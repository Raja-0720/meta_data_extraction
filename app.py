from fastapi import FastAPI
import pickle

app = FastAPI(title="Contract Metadata Extraction API")


model = pickle.load(open("contract_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


@app.post("/extract")
def extract_metadata(text: str):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)

    return {
        "party_one": pred[0][0],
        "party_two": pred[0][1],
        "agreement_value": pred[0][2],
        "start_date": pred[0][3],
        "end_date": pred[0][4],
        "renewal_notice_days": pred[0][5]
    }
