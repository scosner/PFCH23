import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# wonder dates
wonder = pd.DataFrame([['Great Pyramid of Giza', -2584, 2023], 
                    ['Hanging Gardens of Babylon', -600, 100],
                    ['Temple of Artemis at Ephesus', -550, 262],
                    ['Statue of Zeus at Olympia', -466, 450],
                    ['Mausoleum at Halicarnasus', -351,1494],
                    ['Colossus of Rhodes', -292,-226], 
                    ['Lighthouse of Alexandra', -280, 1480]], 
                    columns=['EnglishName', 'Start', 'Finish']) 

event = wonder['EnglishName']
begin = wonder['Start']
end = wonder['Finish']
length =  wonder['Finish'] - wonder['Start']

# chart
fig, ax = plt.subplots(figsize=(12,6))

# bars
bars = ax.barh(range(len(begin)), (end-begin), .3, left=begin, color=['gold', 'red', 'green', 'blue', 'cyan', 'purple', 'black'],)

# Formatting
ax.tick_params(axis='both', which='major', labelsize=15)
ax.tick_params(axis='both', which='minor', labelsize=20)
ax.set_title('Wonders of the Ancient World', fontsize = '25')
ax.set_xlabel('Year', fontsize = '20')
ax.set_yticks(range(len(begin)))
ax.set_yticklabels("")
ax.set_xlim(-2600, 2100)
ax.set_ylim(-1,18)
for i in range(7):
    ax.text(begin.iloc[i] + length.iloc[i]/2, 
             i+.25, event.iloc[i], 
             ha='center', fontsize = '14')

# MPLD3 Interactive Chart
mpld3.plugins.connect(fig, mpld3.plugins.MousePosition(fontsize=14))

# Html Save
mpld3.save_html(fig, 'wonderstimeline.html')

# Display test
mpld3.display()
