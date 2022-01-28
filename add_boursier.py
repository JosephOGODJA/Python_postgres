#!usr/bin/python3

def get_ID_statu_matimonial():
    Statut_Matrimonial = input("Statut Matrimonial : ")
    Conjoint = input("Conjoint : ")
    Enfants_à_charge = input("Enfants à charge : ")
    
    query = ("INSERT INTO statut_matrimonial (Statut_Matrimonial, Conjoint, Enfants_à_charge) VALUES (%s, %s, %s)" % (Statut_Matrimonial, Conjoint, Enfants_à_charge))
    cur.execute(query)
    
    query = ("SELECT ID_statu_matimonial FROM statut_matrimonial WHERE Statut_Matrimonial = %s AND (Conjoint = %s AND Enfants_à_charge = %s)" % (Statut_Matrimonial, Conjoint, Enfants_à_charge))
    cur.execute(query)
    ID_statu_matimonial = cur.fetchone()
    
    return ID_statu_matimonial
    
def get_ID_coordonees():
    Adresse = input("Adresse : ")
    Mail = input("Mail : ")
    Telephone = input("Telephone : ")
    Position_actuelle = input("Position actuelle : ")
    
    query = ("INSERT INTO coordonnees (Adresse, Mail, Telephone, Position_actuelle) VALUES ( %s, %s, %s, %s)" % (Adresse, Mail, Telephone, Position_actuelle))
    cur.execute(query)
    
    query = ("SELECT ID_coordonees FROM coordonnées WHERE (Adresse = %s AND Mail = %s) AND (Telephone = %s AND Position_actuelle = %s)" % (Adresse, Mail, Telephone, Position_actuelle))
    cur.execute(query)
    
    ID_coordonees = cur.fetchone()
    
    return ID_coordonees
    
def get_ID_formation():
    Nom_de_la_formation = input("Nom de la formation : ")
    Pays_de_formation = input("Pays de formation : ")
    Date_de_début = input("Date de début : ")
    Date_de_fin = input("Date de fin : ")
    Diplôme_associé = input("Diplôme associé : ")
    
    query = ("INSERT INTO formation (Nom_de_la_formation, Pays_de_formation, Date_de_début, Date_de_fin, Diplôme_associé) VALUES (%s, %s, %s, %s, %s)" % (Nom_de_la_formation, Pays_de_formation, Date_de_début, Date_de_fin, Diplôme_associé))
    cur.execute(query)
    
    query = ("SELECT ID_formation FROM formation WHERE (Nom_de_la_formation = % AND (Pays_de_formation = %s AND Date_de_début = %s )) AND (Date_de_fin = %s AND Diplôme_associé = %s)" % (Nom_de_la_formation, Pays_de_formation, Date_de_début, Date_de_fin, Diplôme_associé))
    cur.execute(query)
    
    ID_formation = cur.fetchone()
    
    return ID_formation
    
def get_ID_bourse():
    Nom_de_la_bourse = input("Nom de la bourse : ")
    Montant_Alloué = input("Montant Alloué : ")
    Frais_de_vie = input("Frais de vie : ")
    Frais_de_formation = input("Frais de formation : ")
    Deplacement = input("Deplacement : ")
    
    query = ("INSERT INTO bourse (Nom_de_la_bourse, Montant_Alloué, Frais_de_vie, Frais_de_formation, Deplacement) VALUES (%s, %s, %s, %s, %s)" % (Nom_de_la_bourse, Montant_Alloué, Frais_de_vie, Frais_de_formation, Deplacement))
    cur.execute(query)
    
    query = ("SELECT ID_bourse FROM bourse WHERE (Nom_de_la_bourse = %s AND (Montant_Alloué = %s AND Frais_de_vie = %s)) AND (Frais_de_formation = %s AND Deplacement = %s)" % (Nom_de_la_bourse, Montant_Alloué, Frais_de_vie, Frais_de_formation, Deplacement))
    cur.execute(query)
    
    ID_bourse = cur.fetchone()
    
    return ID_bourse
    
def get_ID_experience_pro():
    PosteOccupé = input("Poste = Occupé : ")
    Durée = input("Durée : ")
    Période = input("Période : ")
    
    query = ("INSERT INTO expérience_professionnelle (PosteOccupé, Durée, Période) VALUES (%s, %s, %s)" % (PosteOccupé, Durée, Période))
    cur.execute(query)
    
    query = ("SELECT ID_experience_pro FROM expérience_professionnelle WHERE PosteOccupé = %s AND (Durée = %s AND Période = %s)" % (PosteOccupé, Durée, Période))
    cur.execute(query)
    
    ID_experience_pro = cur.fetchone()
    
    return ID_experience_pro
    
def get_ID_metier():
    Nom_du_métier = input("Nom du métier : ")
    Salaire = input("Salaire : ")
    
    query = ("INSERT INTO metier (Nom_du_métier, Salaire) VALUES (%s, %s)" % (Nom_du_métier, Salaire))
    cur.execute(query)
    
    query = ("SELECT ID_metier FROM metier WHERE Nom_du_métier = %s AND Salaire = %s" % (Nom_du_métier, Salaire))
    cur.execute(query)
    
    ID_metier = cur.fetchone()
    
    return ID_metier

def get_ID_sante():
    Sexe = input("Sexe (en cm) : ") 
    Problème_de_santé = input("Problème de santé : ")
    Traitement_suivi = input("Traitement suivi : ")
    Allergies = input("Allergies : ")
    Conditions_physique = input("Conditions physique : ")
    
    query = ("INSERT INTO santé (Sexe, Problème_de_santé, Traitement_suivi, Allergies, Conditions_physique) VALUES (%s, %s, %s, %s, %s)" % (Sexe, Problème_de_santé, Traitement_suivi, Allergies, Conditions_physique))
    cur.execute(query)
    
    query = ("SELECT ID_sante FROM santé WHERE (Sexe = %s AND (Problème_de_santé = %s AND Traitement_suivi = %s)) AND (Allergies = %s AND Conditions_physique = %s)" % (Sexe, Problème_de_santé, Traitement_suivi, Allergies, Conditions_physique))
    cur.execute(query)
    
    ID_sante  = cur.fetchone()
    
    return ID_sante

def create_boursier():
    Nom = input("Nom : ")
    PrenomBoursier = input("Prenom : ")
    
    ID_statu_matimonial = get_ID_statu_matimonial()
    Coordonnees = get_ID_coordonees()
    Formation = get_ID_formation()
    Bourse = get_ID_bourse()
    ExperienceProfessionnelle = get_ID_experience_pro()
    Metier = get_ID_metier()
    Sante = get_ID_sante()
    
    query = ("INSERT INTO boursier (Nom, PrenomBoursier, ID_statu_matimonial, Coordonnees, Formation, Bourse, ExperienceProfessionnelle, Metier, Sante) VALUES (%s, %s, %d, %d, %d, %d, %d, %d, %d)" % (Nom, PrenomBoursier, ID_statu_matimonial, Coordonnees, Formation, Bourse, ExperienceProfessionnelle, Metier, Sante))
    cur.execute(query)    
