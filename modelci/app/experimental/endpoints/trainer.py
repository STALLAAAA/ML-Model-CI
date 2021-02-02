#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Li Yuanming
Email: yli056@e.ntu.edu.sg
Date: 1/15/2021
"""
from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from modelci.experimental.curd.model_train import save, get_by_id, get_all, delete_by_id, delete_all
from modelci.experimental.finetuner.trainer import PyTorchTrainer
from modelci.experimental.model.model_train import TrainingJob, TrainingJobIn

router = APIRouter()


@router.post('/', status_code=201)
def create_training_job(training_job: TrainingJobIn):
    """
    Create a training job data object, and save it into the database. Then, submit the created training job
    (with job ID generated by database) to the training job coordinator.

    Args:
        training_job (TrainingJobIn): Training job to be submitted.

    Returns:
        Submitted training job data class object.
    """
    id_ = save(training_job_in=training_job)
    if id_ is not None:
        training_job = get_by_id(id_)
        trainer = PyTorchTrainer.from_training_job(training_job)
        trainer.start()
        trainer.join()
    return {'id': str(id_)}


@router.get('/')
def get_all_training_jobs() -> List[TrainingJob]:
    return get_all()


@router.get('/{id}')
def get_training_job(id: str) -> TrainingJob:
    """
    Get a training job.

    Args:
        id (str): Training job ID.

    Returns:
        int: Affected number of records.
    """
    return get_by_id(id)


@router.delete('/{id}')
def delete_training_job(id: str):
    """
    Delete a training job.

    Args:
        id (str): Training job ID.

    Returns:
        int: Affected number of records.
    """
    if bool(delete_by_id(id)):
        return JSONResponse(status_code=204)
    else:
        return JSONResponse(status_code=400, content={'message': 'Failed in deletion.'})


@router.delete('/')
def delete_all_training_job():
    count = delete_all()
    return JSONResponse(status_code=204, content={'deleted': count})
