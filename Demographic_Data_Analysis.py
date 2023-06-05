#this was really hard.  i spent like 9 hours straight on it.  my god

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

  

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = (df[df['sex'] == 'Male']['age'].mean()).round(1)

    # What is the percentage of people who have a Bachelor's degree?
    education_counts = df['education-num'].size
    filtered_bachelors = (df['education-num'] == 13).sum()
    percentage_bachelors = ((filtered_bachelors / education_counts) * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

  
    # What percentage of people without advanced education make more than 50K

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)

    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'].eq(1)]
    n_m_w_s = (df['hours-per-week'].eq(1)).sum()
  
    num_min_rich = (num_min_workers['salary'].eq('>50K')).sum()
   

    rich_percentage = ((num_min_rich/n_m_w_s) *100).round(1)

    # What country has the highest percentage of people that earn >50K?
   # Filter the DataFrame based on salary condition
    rich_df = df[df['salary'].eq('>50K')]
    
    # Calculate the value counts of 'native-country' in the filtered DataFrame
    native_country_counts = rich_df['native-country'].value_counts()
    
    # Calculate the total value counts of 'native-country'
    total_country_counts = df['native-country'].value_counts()
    
    # Calculate the percentage of highest earning individuals in each country
    percentage = ((native_country_counts / total_country_counts) * 100).round(1)
    
    # Get the country with the highest percentage of highest earners
    highest_earning_country = percentage.idxmax()
    highest_earning_country_percentage = percentage.max()



    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = rich_df[rich_df['native-country'] == 'India']['occupation'].mode().values[0]

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
