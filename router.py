from fastapi import APIRouter
from responses import TaskResponses
from schemas import STaskAdd

router = APIRouter(
    prefix='/tasks'
)

@router.post("")
async def add_task(task: STaskAdd):
    tasks = await TaskResponses.add_one(task)
    return {'ok':True, 'task_id': tasks}

@router.get("")
async def get_tasks():
    task =  await TaskResponses.find_all()
    return {"data":task}
