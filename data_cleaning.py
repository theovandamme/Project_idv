import pandas as pd
import numpy as np

# Assuming your data is in a DataFrame called 'df'
df = pd.read_csv('Data/ROLE 1.0 Data Release JPR SU21 Final/ROLE 1.0 Data Release JPR SU21 Final.csv')  # or however you're loading your data
df.fillna('none')

# Define how to aggregate each column
agg_dict = {
    'rolecode': 'first',
    'professionaltitle': lambda x: ', '.join(x.dropna().unique()),
    'militaryrank': lambda x: ', '.join(x.dropna().unique()),
    'culturaltitle': lambda x: ', '.join(x.dropna().unique()),
    'religioustitle': lambda x: ', '.join(x.dropna().unique()),
    'fullbirthname': 'first',
    'popularname': 'first',
    'nameone': 'first',
    'nametwo': 'first',
    'nomdeguerrekunya': lambda x: ', '.join(x.dropna().unique()),
    'alsoknownasaka': lambda x: ', '.join(x.dropna().unique()),
    'stname': 'first',
    'confdesc': 'first',
    'groupname': 'first',
    'altname': lambda x: ', '.join(x.dropna().unique()),
    'revmodcode': 'first',
    'gender': 'first',
    'yearofbirth': 'first',
    'yearofdeath': 'last',  # Take the latest year of death
    'dead': 'last',  # Take the latest dead status
    'placeofbirth': 'first',
    'leadershipage': 'first',
    'dynamicage': 'first',  # Take the latest dynamic age
    'entrymethod': lambda x: ', '.join(x.dropna().unique()),
    'powersharing': 'first',
    'education': lambda x: ', '.join(x.dropna().unique()),
    'areaofstudy': lambda x: ', '.join(x.dropna().unique()),
    'cat_areaofstudy1': lambda x: ', '.join(x.dropna().unique()),
    'cat_areaofstudy2': lambda x: ', '.join(x.dropna().unique()),
    'educusuk': 'max',
    'educwest': 'max',
    'married': 'max',
    'marriageage': 'first',
    'children': 'max',
    'religion': 'first',
    'family': 'first',
    'affiliation': 'last',
    'physical': 'first',
    'mental': 'first',
    'occupation': lambda x: ', '.join(x.dropna().unique()),
    'military': 'max',
    'nsmilitary': 'max',
    'combat': 'max',
    'govpost': 'max',
    'exile': 'max',
    'studyab': 'max',
    'studyab_yr_total': 'max',
    'studyab_level': lambda x: ', '.join(x.dropna().unique()),
    'studyab_countries': lambda x: ', '.join(x.dropna().unique()),
    'milab': 'max',
    'workab': 'max',
    'expabroad': 'max',
    'prison': 'max',
    'assassin': 'max',
    'deathcause': lambda x: ', '.join(x.dropna().unique()),  # Take the latest death cause
    'languages': lambda x: ', '.join(x.dropna().unique()),
    'english': 'max',
    'polyglot': 'max',
    'status': 'last',  # Take the latest status
    'gscholar': 'first',
    'year': lambda x: f"{min(x)}-{max(x)}",  # Show range of years
    'duration': 'sum',
    'observation': 'last',
    'ldrnum': 'first',
    'ldrstwar_month': 'first',
    'ldrstwar_year': 'first',
    'ldrendwar_month': 'last',
    'ldrendwar_year': 'last',
    'conflictid': 'first',
    'dyadid': 'first',
    'actorid': 'first',
    'incompatibility': 'first',
    'intensitylevel': 'max',
    'terrcont': 'max',
    'prevactive': 'max',
    'rebstrength': 'last',  # Take the latest rebel strength
    'strengthcent': 'last',  # Take the latest strength cent
    'k_a': 'sum',
    'km_a': 'sum',
    't_a': 'sum',
    'tm_a': 'sum',
    'diaspora': 'max',
    'finance': 'last',
    'nagtheo': 'max',
    'nag_support': 'max',
    'islamist': 'max',
    'stdcinc': 'last',
    'xpolity': 'last',
    'rgdppc': 'last',
    'ccode': 'first',
    'africa': 'max',
    'asia': 'max',
    'europe': 'max',
    'mena': 'max',
    'americas': 'max'
}

# Group by leadercode and aggregate
df_unique = df.groupby('leadercode').agg(agg_dict).reset_index()

# Add a new column with the last dynamicage value
df_unique['last_dynamicage'] = df.groupby('leadercode')['dynamicage'].last().values

# After creating df_unique, load the region data
region_data = pd.read_csv('Data/world_regions.csv', sep=';')

# Rename columns if necessary to match your main data
region_data = region_data.rename(columns={
    'Entity': 'stname', 
    'Sustainable Development Goals (SDG) Regions': 'Region'
})

# Merge the region data with your main data
df_unique_with_region = pd.merge(df_unique, region_data[['stname', 'Region']], on='stname', how='left')

# If some countries don't have a match, you might want to fill NaN values
df_unique_with_region['Region'] = df_unique_with_region['Region'].fillna('Unknown')

# Reorder columns if needed
columns_order = ['leadercode', 'stname', 'Region'] + [col for col in df_unique_with_region.columns if col not in ['leadercode', 'stname', 'Region']]
df_unique_with_region = df_unique_with_region[columns_order]

# Display the result
print(df_unique_with_region)

# Save the result to a new CSV file
df_unique_with_region.to_csv('Data/unique_leaders.csv', index=False,)