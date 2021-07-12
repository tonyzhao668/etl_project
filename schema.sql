-- Create Two Tables
REATE TABLE roadworks_details(
  Id int PRIMARY KEY,
  StartDate Date,
  FinishDate Date,
  WorkType varchar(250),
  Suburb varchar(250),
  Road varchar(250),
  Region varchar(250),
  TrafficImpact varchar(250) 
);


