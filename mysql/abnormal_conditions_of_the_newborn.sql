CREATE TABLE IF NOT EXISTS
	abnormal_conditions_of_the_newborn 
AS
SELECT 
	id,DOB_YY,AB_AVEN1,AB_AVEN6,AB_SURF,AB_ANTI,AB_SEIZ,F_AB_VENT,F_AB_VENT6,F_AB_NIUC,F_AB_SURFAC,F_AB_ANTIBIO,F_AB_SEIZ,NO_ABNORM,AB_NICU
FROM 
	cdcnatality.all_years_data;