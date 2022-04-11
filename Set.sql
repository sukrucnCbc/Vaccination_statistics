SELECT * FROM [dbo].[country_vaccination_stats]

UPDATE [dbo].[country_vaccination_stats] SET [daily_vaccinations]  = 0 WHERE [daily_vaccinations] IS NULL


SELECT [daily_vaccinations],[vaccines] FROM [dbo].[country_vaccination_stats]
GROUP BY [daily_vaccinations],[vaccines] 
