import doc_parser, SQL_updater, MySQLdb

#####################################################################
########################## Biomarker-Disease ##############################
#####################################################################
def BiomarkerDiseaseRelationUploader(gt, relations, filename):
    database = MySQLdb.connect("canaryctr-donald.stanford.edu", "markerville_user", "b1omark3rsRock!", "MARKERVILLE")
    good_predictions = []
    count = 0
    while count < len(gt):
        if(gt[count] == 1 or gt[count] == 0):
            good_predictions.append(relations[count])
    for prediction in good_predictions:
        biomarker = doc_parser.listToString(prediction.mention1(attribute="words"))
        disease = doc_parser.listToString(prediction.mention2(attribute="words"))
        bioID = SQL_updater.add_biomarker(biomarker)
        diseaseID = SQL_updater.add_disease(disease)
        sourceID = SQL_updater.add_source("ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/" + filename)
        SQL_updater.add_relation(db=database, biomarkerID=bioID, diseaseID=diseaseID, sourceID=sourceID)

#####################################################################
############################ Biomarker- Medium ###########################
#####################################################################