# Environment variables details

## HARVEST_ACCOUNT_ID
* [harvest credentials](harvest.md)

## HARVEST_AUTHORIZATION
* [harvest credentials](harvest.md)

## BEGIN_DATE
The first day you want to count "**included**"

## END_DATE
The last day you want to count "**included**"

## HOURS_PER_WORK_DAY
where 7.5 is 7 hours and 30 minutes

## WORK_DAYS_OF_THE_WEEK
0 is monday

## WORKED_HOURS_CORRECTION (optional)
Number of hours to add to your total worked time from harvest. Can be negative.  
Ex: 35 hours of overtime where paid by your boss: WORKED_HOURS_CORRECTION=-35  
Ex: You took a 35h week of unpaid vacation that is not written in harvest: WORKED_HOURS_CORRECTION=35
