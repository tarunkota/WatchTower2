from Core.crons import *
from Core.tasks import *
metric = Metric.objects.get(pk=1)
# getMetricValue(metric)
# getAllMetricValues(metric.frequency)
# getAllModuleValues(metric.frequency)
getAllModuleValues(Frequency.objects.get(pk=2))


everyMinuteCron()


curl - H "Authorization: Token 21b206df29ff8cab106f4c5246b2ea630dc3c7a7" 'http://localhost:9000/api/metrics/?project=Naulets&metric=Test&count=10'

curl - H "Authorization: Token 21b206df29ff8cab106f4c5246b2ea630dc3c7a7" 'http://localhost:9000/api/module/?project=Naulets&module=Test'


sudo - u postgres psql
CREATE DATABASE watchtower
CREATE USER watchtoweruser WITH PASSWORD 'aebvare'

ALTER ROLE watchtoweruser SET client_encoding TO 'utf8'
ALTER ROLE watchtoweruser SET default_transaction_isolation TO 'read committed'
ALTER ROLE watchtoweruser SET timezone TO 'UTC'

GRANT ALL PRIVILEGES ON DATABASE watchtower TO watchtoweruser
