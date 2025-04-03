import re
import json
from pydantic import BaseModel, ValidationError, Field
from typing import Literal


class OutputData(BaseModel):
    """Represents the validated output data."""
    Hospital_Benefit: int = Field(alias="Hospital Benefit", gt=0)
    Personal_Accident: int = Field(alias="Personal Accident", gt=0)
    Standard_Sports_and_Activities: Literal["Included", "Not Included"] = Field(alias="Standard Sports and Activities")


def validate_output_pydantic(response: str) -> OutputData:
    """Validate the output from the model using Pydantic.
    Args:
        response (str): The output from the model.
    Returns:
        OutputData: The validated output as a Pydantic model.
    Raises:
        ValueError: If the input string does not contain a valid JSON object,
                    or if the parsed JSON does not conform to the OutputData model.
    """
    match = re.search(r'\{.*\}', response, re.DOTALL)
    if not match:
        raise ValueError("The input string does not contain a valid JSON object.")
    
    json_str = match.group(0)
    try:
        parsed_data = json.loads(json_str)
    except json.JSONDecodeError:
        raise ValueError("The extracted string is not a valid JSON object.")
    
    try:
        return OutputData(**parsed_data)
    except ValidationError as e:
        raise ValueError(str(e))
