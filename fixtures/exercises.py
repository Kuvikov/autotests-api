import pytest
from pydantic import BaseModel

from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, ExerciseSchema
from fixtures.users import UserFixture
from fixtures.courses import CourseFixture
from clients.exercises.exercises_client import get_exercises_client, ExercisesClient


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

    @property
    def exercise(self) -> ExerciseSchema:
        return self.response.exercise

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
    function_course: CourseFixture,
    exercises_client: ExercisesClient,
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(courseId=function_course.course.id)
    response = exercises_client.create_exercise(request)

    return ExerciseFixture(request=request, response=response)
