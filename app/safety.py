def needs_plan_details(question):
    text = question.lower()

    plan_specific_terms = [
        "does my insurance cover",
        "does my health insurance cover",
        "is my treatment covered",
        "is this covered by my plan",
        "will my insurance pay",
        "my monthly premium",
        "exact monthly premium",
        "my copay",
        "my coinsurance",
        "my out-of-pocket",
        "my insurance plan",
        "my exact monthly health insurance premium",
        "my monthly health insurance premium",
    ]

    return any(term in text for term in plan_specific_terms)


def plan_details_response():
    return (
        "I need more information about your specific health insurance plan "
        "to answer this accurately. Coverage and costs depend on your plan. "
        "Please share your plan name and relevant coverage details, "
        "or check directly with your insurance provider."
    )
