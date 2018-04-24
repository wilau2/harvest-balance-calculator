FROM williamlauze/harvest-balance-calculator-common:latest

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
RUN pip3 install pycodestyle
RUN pip3 install codecov

#Needed for codecov
COPY .git /www

COPY ./ /www

WORKDIR www

CMD python3 src/main.py