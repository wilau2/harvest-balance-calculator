FROM williamlauze/harvest-balance-calculator-infra:latest

COPY src /www

WORKDIR www

CMD python3 main.py