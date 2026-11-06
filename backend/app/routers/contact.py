from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(tags=["contact"])


@router.post("/contact", response_model=schemas.ContactOut, status_code=201)
def send_message(payload: schemas.ContactIn, db: Session = Depends(get_db)):
    message = models.Message(
        name=payload.name.strip(),
        email=payload.email,
        subject=payload.subject.strip(),
        message=payload.message.strip(),
    )
    db.add(message)
    db.commit()
    db.refresh(message)

    return schemas.ContactOut(
        ok=True,
        message="Terima kasih! Pesanmu sudah terkirim.",
        sent_at=datetime.now(timezone.utc),
    )
