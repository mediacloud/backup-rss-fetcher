from __future__ import absolute_import
from celery import Celery
import logging

from fetcher import BROKER_URL, BACKEND_URL

logger = logging.getLogger(__name__)

# we use celery to support parallel processing of stories in need of classification
app = Celery('backup-rss-fetcher',
             broker=BROKER_URL,
             backend=BACKEND_URL,
             include=['fetcher.tasks'])
