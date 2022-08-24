import survey
import numpy as np
import pandas as pd


def get_pregnancies_df():
    table = survey.Pregnancies()
    table.ReadRecords()

    pregnancies_list = []

    for rec in table.records:
        pregnancies_list.append(
            [
                chk(rec.caseid),
                chk(rec.nbrnaliv),
                chk(rec.babysex),
                chk(rec.birthwgt_lb),
                chk(rec.birthwgt_oz),
                chk(rec.prglength),
                chk(rec.outcome),
                chk(rec.birthord),
                chk(rec.agepreg),
                chk(rec.finalwgt),
            ]
        )

    pregnancies_df = pd.DataFrame(
        pregnancies_list,
        columns=[
            "caseid",
            "nbrnaliv",
            "babysex",
            "birthwgt_lb",
            "birthwgt_oz",
            "prglength",
            "outcome",
            "birthord",
            "agepreg",
            "finalwgt",
        ],
    )

    return pregnancies_df


def chk(obj):
    if obj == "NA" or obj == "na":
        return np.nan

    return obj


if __name__ == '__main__':
    df = get_pregnancies_df()
    df.to_csv('pregnancies.csv', index=False)
