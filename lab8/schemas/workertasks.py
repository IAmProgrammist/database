from schemas.base import TunedModel


class WorkerTasksIdentifier(TunedModel):
    worker_inn: str
    task_id: int


class WorkerTasksCreate(WorkerTasksIdentifier):
    pass


class WorkerTasksShow(WorkerTasksIdentifier):
    pass
