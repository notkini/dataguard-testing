from dataguard import validate_csv

report = validate_csv(
    "test.csv",
    target="Survived",
    signal=True
)

report.summary()
