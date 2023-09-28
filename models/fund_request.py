from config import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Text
from datetime import datetime

# Define the database models
class FundRequest(db.Model):
    __tablename__ = 'fund_request'

    id = db.Column(db.Integer, primary_key=True)
    request_track_id = db.Column(db.String(25), nullable=False)
    itineraire = db.Column(db.String(255), nullable=False)
    moyen_de_transport = db.Column(db.String(25), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    but_de_la_mission = db.Column(db.String(255), nullable=False)
    nom_prenoms_chauffeur = db.Column(db.String(255), nullable=False)
    approval_level = db.Column(db.Integer, nullable=False, default=1)
    reject_reason = db.Column(db.Text, nullable=True, default=None)
    date_debut = db.Column(db.Date, nullable=False)
    date_fin = db.Column(db.Date, nullable=False)
    superieur_hierarchique_username = db.Column(db.String(100), nullable=True)
    dga_username = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'),nullable=False)
    domaine_activite_id = db.Column(db.Integer, db.ForeignKey('activity_domain.id'),nullable=False)
    centre_de_cout_id = db.Column(db.Integer, db.ForeignKey('cost_center.id'),nullable=False)
    request_approval_dts = db.relationship('RequestApprovalDatetime', backref='fund_request', lazy=True)

    def __init__(self, itineraire, moyen_de_transport, zone_id, but_de_la_mission, nom_prenoms_chauffeur, date_debut, date_fin, domaine_activite_id, centre_de_cout_id, sup_hier, dga):
        self.request_track_id = ""
        self.itineraire = itineraire
        self.moyen_de_transport = moyen_de_transport
        self.nom_prenoms_chauffeur = nom_prenoms_chauffeur
        self.zone_id = zone_id
        self.but_de_la_mission = but_de_la_mission
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.domaine_activite_id = domaine_activite_id
        self.centre_de_cout_id = centre_de_cout_id
        self.superieur_hierarchique_username = sup_hier
        self.dga_username = dga

    def serialize(self):
        return {
            'id': self.id,
            'request_track_id': self.request_track_id,
            'itineraire': self.itineraire,
            'moyen_de_transport': self.moyen_de_transport,
            'but_de_la_mission': self.but_de_la_mission,
            'reject_reason': self.reject_reason,
            'nom_prenoms_chauffeur': self.nom_prenoms_chauffeur,
            'superieur_hierarchique':self.superieur_hierarchique_username,
            'dga_username':self.dga_username,
            'date_debut': self.date_debut,
            'date_fin': self.date_fin,
            'approval_level': self.approval_level,
            'status': self.status,
            'zone': self.zone.serialize(),
            'domaine_activite': self.activity_domain.serialize(),
            'centre_de_cout': self.cost_center.serialize()
        }