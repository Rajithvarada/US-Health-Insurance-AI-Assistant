
import boto3
import json
import os

from phase10.app.safety import (
    needs_plan_details,
    plan_details_response,
)

AWS_REGION = "ap-southeast-2"

ENDPOINT_NAME = os.getenv(
    "SAGEMAKER_ENDPOINT_NAME",
    "us-health-insurance-ai-endpoint-g6"
)


def get_sagemaker_runtime():
    return boto3.client(
        "sagemaker-runtime",
        region_name=AWS_REGION
    )


def ask_sagemaker(question):
    if not isinstance(question, str) or not question.strip():
        return "Please enter a health insurance question."

    question = question.strip()

    if len(question) > 2000:
        return "Please keep your question under 2,000 characters."

    if needs_plan_details(question):
        return plan_details_response()

    try:
        runtime = get_sagemaker_runtime()

        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType="application/json",
            Accept="application/json",
            Body=json.dumps({"question": question})
        )

        raw_result = response["Body"].read().decode("utf-8")
        result = json.loads(raw_result)

        if isinstance(result, list):
            result = json.loads(result[0])

        if isinstance(result, str):
            result = json.loads(result)

        return result.get(
            "answer",
            "Sorry, no answer was returned by the model."
        )

    except Exception as error:
        print(f"SageMaker inference error: {error}")
        return (
            "Unable to connect to the AI service right now. "
            "Please try again later."
        )
