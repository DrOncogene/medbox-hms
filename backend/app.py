#!/usr/bin/env python3
"""
"""

from storage import db

from models.notes.generic_note import Note

note = Note()

db.new(note)
db.save()
