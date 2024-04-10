import pandas as pd

# NOTE: 
# Code validé par les tests de freeCodeCamp
# Peut clairement être amélioré !
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    males_df = df[df['sex'] == 'Male']
    temp = males_df['age'].mean()
    average_age_men = round(temp, 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_df = df[df['education'] == 'Bachelors']
    temp = (len(bachelors_df) / len(df)) * 100
    percentage_bachelors = round(temp, 1)

    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # On calcule le nombre d'individus avec une éducation supérieure
    with_bachelors = df['education'] == 'Bachelors'
    with_masters = df['education'] == 'Masters'
    with_doctorate = df['education'] == 'Doctorate'
    higher_education_df = df[with_bachelors | with_masters | with_doctorate]
    # Puis, on sélectionne ceux qui ont un salaire >50K
    hes50Kplus_df = higher_education_df[higher_education_df['salary'] == '>50K']
    # Enfin, on calcule le pourcentage
    h = (len(hes50Kplus_df) / len(higher_education_df)) * 100
    higher_education = round(h, 1)
    
    # On fait les mêmes opérations pour les individus sans éducation supérieure
    lower_education_df = df[~with_bachelors & ~with_masters & ~with_doctorate]
    les50Kplus_df = lower_education_df[lower_education_df['salary'] == '>50K']
    l = (len(les50Kplus_df) / len(lower_education_df)) * 100
    lower_education = round(l, 1)

    # percentage with salary >50K
    higher_education_rich = round(h, 1)
    lower_education_rich = round(l, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers_df = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = len(min_workers_df)

    rich_min_workers_df = min_workers_df[min_workers_df['salary'] == '>50K']
    r = (len(rich_min_workers_df) / num_min_workers) * 100
    rich_percentage = round(r, 1)

    # What country has the highest percentage of people that earn >50K?
    with_high_salary = df['salary'] == '>50K'
    high_earners_df = df[with_high_salary]
    temp_df = (high_earners_df['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = temp_df.idxmax()
    highest_earning_country_percentage = round(temp_df.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    fifty_k_plus_df = df[df['salary'] == '>50K']
    fifty_k_plus_df_in_india = fifty_k_plus_df[fifty_k_plus_df['native-country'] == 'India']
    top_IN_occupation = fifty_k_plus_df_in_india['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
