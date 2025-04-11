from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class ContentSource(db.Model):
    """Represents a source of healthcare information (social media post, news article, etc.)"""
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512))
    source_type = db.Column(db.String(50))
    content = db.Column(db.Text)
    title = db.Column(db.String(500))  # For news articles
    author = db.Column(db.String(200))
    published_date = db.Column(db.DateTime)
    retrieved_date = db.Column(db.DateTime, default=datetime.utcnow)
    region = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    classifications = db.relationship('ContentClassification', backref='source', lazy=True)
    
    def __repr__(self):
        return f'<ContentSource {self.source_type}: {self.url}>'

class ContentClassification(db.Model):
    """Classification of healthcare content as true, false, or misleading"""
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('content_source.id'))
    classification = db.Column(db.String(50))
    confidence_score = db.Column(db.Float)
    healthcare_topic = db.Column(db.String(100))
    classified_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContentClassification {self.classification} ({self.confidence_score})>'

class MisinformationTrend(db.Model):
    """Tracks trends in healthcare misinformation over time"""
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    region = db.Column(db.String(100))
    trend_date = db.Column(db.DateTime, default=datetime.utcnow)
    impact_score = db.Column(db.Float)
    
    def __repr__(self):
        return f'<MisinformationTrend {self.topic} - {self.region} - {self.trend_date}>'

class FactCheckEntry(db.Model):
    """Database of fact-checked healthcare claims"""
    id = db.Column(db.Integer, primary_key=True)
    claim = db.Column(db.Text)
    fact = db.Column(db.Text)
    source = db.Column(db.String(512))
    rural_relevance = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<FactCheckEntry {self.claim[:50]}...>'

class Report(db.Model):
    """User-submitted reports of healthcare misinformation"""
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    content_text = db.Column(db.Text)
    reporter_email = db.Column(db.String(120))
    report_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='pending')  # 'pending', 'verified', 'false_report'
    region = db.Column(db.String(100))
    healthcare_topic = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Report {self.url} - {self.status}>'
