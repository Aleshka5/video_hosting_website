from sqlalchemy import Column, Integer, Text, ForeignKey
from dataclasses import dataclass

from sqlalchemy.orm import relationship
from humps import camel

from app import db

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=False)
    password = Column(Text, unique=False)
    telegram = Column(Text, unique=True)
    loyalty = Column(Integer)

    def __init__(self, name=None, telegram=None, password=None, loyalty=0):
        self.name = name
        self.password = password
        self.telegram = telegram
        self.loyalty = loyalty

    def as_dict(self):
        return {camel.case(c.name): getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<id {}>'.format(self.id)

@dataclass
class Video(db.Model):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    video_name = Column(Text, unique=False)
    video_description = Column(Text, unique=False)
    video_category = Column(Text, unique=False)
    video_preview_path = Column(Text, unique=False)
    video_file_path = Column(Text, unique=False)
    duration_seconds = Column(Integer)
    fps = Column(Integer)
    scenes = db.relationship('Scene', backref='videos')

    def __init__(
            self,
            video_name=None,
            video_description=None,
            video_category=None,
            video_preview_path=None,
            video_file_path=None,
            duration_seconds=0,
            fps=0):
        self.video_name = video_name
        self.video_description = video_description
        self.video_category = video_category
        self.video_preview_path = video_preview_path
        self.video_file_path = video_file_path
        self.duration_seconds = duration_seconds
        self.fps = fps

    def as_dict(self):
        return {camel.case(c.name): getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<id {}>'.format(self.id)

@dataclass
class Scene(db.Model):
    __tablename__ = 'scenes'
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey('videos.id'))
    start_frame = Column(Integer)
    end_frame = Column(Integer)
    subtitles = db.relationship('Subtitle', backref='scenes')
    # video = relationship('Video', foreign_keys='Scene.video_id')

    def __init__(self, video_id=0, start_frame=0, end_frame=0):
        self.video_id = video_id
        self.start_frame = start_frame
        self.end_frame = end_frame

    def as_dict(self):
        return {camel.case(c.name): getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<id {}>'.format(self.id)

@dataclass
class Subtitle(db.Model):
    __tablename__ = 'subtitles'
    id = Column(Integer, primary_key=True)
    scene_id = Column(Integer, ForeignKey('scenes.id'))
    text_subtitle = Column(Text, unique=False)
    voice_file_path = Column(Text, unique=False)
    start_frame = Column(Integer)
    end_frame = Column(Integer)

    # scene = relationship('Scene', foreign_keys='Subtitle.scene_id')

    def __init__(self, scene_id=None, text_subtitle=None, voice_file_path=None, start_frame=0, end_frame=0):
        self.scene_id = scene_id
        self.text_subtitle = text_subtitle
        self.voice_file_path = voice_file_path
        self.start_frame = start_frame
        self.end_frame = end_frame

    def as_dict(self):
        return {camel.case(c.name): getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<id {}>'.format(self.id)
