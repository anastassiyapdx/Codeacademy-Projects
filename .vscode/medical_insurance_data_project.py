# Importing csv module to work with csv files
import csv

# Opening file with insurance costs data
with open('insurance.csv') as insurance_csv:
    print(insurance_csv.read())

# Creating lists to put each row of data in csv
with open('insurance.csv') as insurance_csv:
    insurance_file = csv.DictReader(insurance_csv)
    age_list = []
    sex_list = []
    bmi_list = []
    children_list = []
    smoker_list = []
    region_list = []
    charges_list = []
    for number in insurance_file:
        age_list.append(int(number['age']))
        sex_list.append(number['sex'])
        bmi_list.append(float(number['bmi']))
        children_list.append(int(number['children']))
        smoker_list.append(number['smoker'])
        region_list.append(number['region'])
        charges_list.append(float(number['charges']))

# Creating a list, so each patient has a number
patients_list = []
for x in range(1, 1339):
    patients_list.append(x)
#print(patients_list)

# Creating the dictionary with all of the data from csv
def insurance_dictionary(patients_list, age_list, sex_list, bmi_list, children_list, smoker_list, region_list, charges_list):
    insurance_dict = {}
    num_patients = len(patients_list)
    for p in range(num_patients):
        insurance_dict[patients_list[p]] = {"Patient_number": patients_list[p], "Age": age_list[p], "Sex": sex_list[p], "Bmi": bmi_list[p], "Children": children_list[p], "Smoker": smoker_list[p], "Region": region_list[p], "Charges": charges_list[p]}
    return insurance_dict

# Checking if the dictionary works fine
insurance_dict = insurance_dictionary(patients_list, age_list, sex_list, bmi_list, children_list, smoker_list, region_list, charges_list)
#print(insurance_dict)

# This function will help us to understand which region has more/less smokers. 
def the_most_smoking(insurance_dict):
    areas = []
    smoking_areas = []
    for patient in insurance_dict:
        areas.append(insurance_dict[patient]["Region"])
        nw = areas.count("northwest")
        sw = areas.count("southwest")
        ne = areas.count("northeast")
        se = areas.count("southeast")
        if insurance_dict[patient]["Smoker"] == "yes":
            smoking_areas.append(insurance_dict[patient]["Region"])
        nw_smoking = smoking_areas.count("northwest")
        sw_smoking = smoking_areas.count("southwest")
        ne_smoking = smoking_areas.count("northeast")
        se_smoking = smoking_areas.count("southeast")
    nw_rate = round((nw_smoking / nw) * 100)
    sw_rate = round((sw_smoking / sw) * 100)
    ne_rate = round((ne_smoking / ne) * 100)
    se_rate = round((se_smoking / se) * 100)
    return nw_rate, sw_rate, ne_rate, se_rate

smoking = the_most_smoking(insurance_dict)
print(smoking)
# We can see that 18% of insured people in the Northwest are smokers. The same is in the Southwest. In the Northeast there are 21% of smokers. The most smoking area is Southeast. There are 25% of smokers."

# Importing statistics module
import statistics

# This function will help us to check if there's a correlation between smoking and bmi. 
def bmi_smoking(insurance_dict):
    people_smoking = []
    people_non_smoking = []
    men_smoking = []
    men_non_smoking = []
    women_smoking = []
    women_non_smoking = []
    for patient in insurance_dict:
        if insurance_dict[patient]["Smoker"] == "yes":
            people_smoking.append(insurance_dict[patient]["Bmi"])
        if insurance_dict[patient]["Smoker"] == "no":
            people_non_smoking.append(insurance_dict[patient]["Bmi"])
        if insurance_dict[patient]["Sex"] == "male" and insurance_dict[patient]["Smoker"] == "yes":
            men_smoking.append(insurance_dict[patient]["Bmi"])
        if insurance_dict[patient]["Sex"] == "male" and insurance_dict[patient]["Smoker"] == "no":
            men_non_smoking.append(insurance_dict[patient]["Bmi"])
        if insurance_dict[patient]["Sex"] == "female" and insurance_dict[patient]["Smoker"] == "yes":
            women_smoking.append(insurance_dict[patient]["Bmi"])
        if insurance_dict[patient]["Sex"] == "female" and insurance_dict[patient]["Smoker"] == "no":
            women_non_smoking.append(insurance_dict[patient]["Bmi"])
    median_people_smoking = statistics.median(people_smoking)
    median_people_non_smoking = statistics.median(people_non_smoking)
    median_men_smoking = statistics.median(men_smoking)
    median_men_non_smoking = statistics.median(men_non_smoking)
    median_women_smoking = statistics.median(women_smoking)
    median_women_non_smoking = statistics.median(women_non_smoking)
    return median_people_smoking, median_people_non_smoking, median_men_smoking, median_men_non_smoking, median_women_smoking, median_women_non_smoking

smoking_bmi = bmi_smoking(insurance_dict)
print(smoking_bmi)
# We can see that difference between the bmis of smokers and non-smokers is minor. However, situation is different for males and females. Female smokers have lower bmi than female non-smokers. Male smokers have higher bmi than male non-smokers.

# This function will count how many people have / don't have children
def children_count(insurance_dict):
    no_children = []
    one_child = []
    two_children = []
    more_children = []
    for patient in insurance_dict:
        if insurance_dict[patient]["Children"] == 0:
            no_children.append(insurance_dict[patient])
        if insurance_dict[patient]["Children"] == 1:
            one_child.append(insurance_dict[patient])
        if insurance_dict[patient]["Children"] == 2:
            two_children.append(insurance_dict[patient])
        if insurance_dict[patient]["Children"] >= 3:
            more_children.append(insurance_dict[patient])
    no_children_count = len(no_children)
    one_child_count = len(one_child)
    two_children_count = len(two_children)
    more_children_count = len(more_children)
    return no_children_count, one_child_count, two_children_count, more_children_count

children_how_many = children_count(insurance_dict)
print(children_how_many)
# We can see that most of the people don't have children. When people have children, having one child is more common than having two or more. 
