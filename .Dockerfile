FROM public.ecr.aws/lambda/python:3.9 as build
COPY . .


FROM public.ecr.aws/lambda/python:3.9

ARG APP_URL
ENV APP_URL ${APP_URL}

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY ${OPENAI_API_KEY}

ARG TELEGRAM_TOKEN
ENV TELEGRAM_TOKEN ${TELEGRAM_TOKEN}

ARG TELEGRAM_URL_API
ENV TELEGRAM_URL_API ${TELEGRAM_URL_API}

COPY --from=build ${LAMBDA_TASK_ROOT}/requirements.txt ${LAMBDA_TASK_ROOT}/requirements.txt
COPY --from=build ${LAMBDA_TASK_ROOT}/app/ ${LAMBDA_TASK_ROOT}/app

RUN pip3 install -r ${LAMBDA_TASK_ROOT}/requirements.txt --target ${LAMBDA_TASK_ROOT}

CMD [ "app.main.handler" ]