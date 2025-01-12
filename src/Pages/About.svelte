<script>
    let value =''
    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'

    
    $: console.log(value)
    </script>
    <div class="text-container">
    <h1>
      About of the Webpage / Project Report
    </h1>

    <h2>
      Introduction
    </h2>
    <p>As part of the Interactive Data Visualization course, a project was created to explore and visualize information about rebel leaders. This study by Acosta et al. (2022) aims to shed light on various aspects of their lives, providing a better understanding of who they are. The aim is to answer key questions such as: Who are they? What drives them? What were their lives like before they became rebel leaders? Do they have children? What is the spatial distribution over the world of those rebel leaders? In essence, the goal is with this project to gain deeper insights into the characteristics of rebel leaders around the world and understand them better, all through an interactive and engaging experience. </p>
    <p>The data used in this project is sourced from Acosta et al. (2022), who created a database detailing the attributes of rebel leaders involved in armed conflicts. Because earlier studies about this topic rarely examined whether and how rebel leader characteristics matter for explaining political outcomes, they developed this database. It contains however variables from earlier research on rebel organizations, from the TAC database (Terrorism in Armed Conflict) from Fortna et al. (2020), such as the annual fatalities made by the use of terrorism for each organization. Acosta proposes that the personal backgrounds and experiences of rebel leaders play a crucial role in explaining the behavior of the rebel organizations they lead. The Rebel Organization Leaders (ROLE) database contains a wide range of biographical information on all top rebel leaders in civil wars that occurred between 1980 and 2011. One of the main goals of the paper and the creation of the database is to shift the focus beyond analyzing rebel organizations and campaigns and bring individual leaders more fully into modern conflict and peace studies (Acosta et al., 2022).</p>
    <p>The project visualizes the results using various types of charts, such as histograms and other graphical representations. The visualizations are designed to allow users to explore detailed charts for each world region. Additionally, automated info sheets for individual rebel leaders were created, providing a dedicated profile for each leader.</p>

    <h2>
      Content of the Project 
    </h2>
    <p>The visible parts (the pages):</p>
    <ul> 
      <li>Overview.svelte: The start webpage that provides an interactive introduction for viewers. All the rebel leaders are represented as points, and they are categorized by different subdivisions, such as world regions, with each category color-coded.</li>
      <li>Charts.svelte: The webpage with all the charts made. The users can choose from one of five elements they want to visualize in a chart: leadership age vs years in power, fatalities vs education and combat experience, education level, fatalities and duration of conflicts, and the leader's occupation before becoming a rebel leader.</li>
      <li>Search.svelte: The webpage where the search bar can be used to look up the name of a rebel leader. When the name of a rebel leader is entered, an info sheet appears with key information and characteristics about the individual.</li>
      <li>About.svelte: The about webpage where information can be found about this project and the webpage. This is also known as the project report.</li>
    </ul>
    <p> The invisible parts (graphs, helpers, data):</p> 
    <ul>
      <li>Graphs:
        <ul>
          <li>AgeVSLeadershipDuration.svelte</li>
          <li>Education.svelte</li>
          <li>FatalCombatEduc.svelte</li>
          <li>Occupation.svelte</li>
          <li>Overview_graph.svelte</li>
        </ul>
      </li>
      <li>Helpers:
        <ul>
          <li>ExportCSV.svelte: To download the rebel leader csv file for a specific world region in the charts section.</li>
          <li>ExportSVG.svelte: To download the visible chart in the charts section.</li>
          <li>WorldRegionExport.js</li>
        </ul>
      </li>
      <li>Data:
        <ul>
          <li>unique_leaders.csv</li>
          <li>world_regions.csv</li>
          
        </ul>
      </li>
    </ul>

    <h2>
      Design Choices
    </h2>
    <p>Design choices regarding lay-out and style were made as follows:</p>
    <ul> 
      <li><b>Text:</b> For font-family there was opted fort a sans-serif font for the global web page, except some graphs, as this results generally in better readability on digital media.</li>
      <li><b>Colors:</b> Neutral dark greens were chosen as color scheme for the project. There was mainly focused on the practical aspects of the functionality of the projects, if there was more time, we might have dug deeper into finding even more suitable color schemes or even backgrounds. Darkened color schemes from D3 were used for region identification in the graphs and on the world map. The color coding for graphs and world map however does not correspond yet. This may have been fixed with more time.</li>
      <li><b>Lay-out:</b> We opted for the use of different pages to have deeper and more complex user interactions with the dataset and make clear distinctions between different purposes on the site. The search page and about page were put in a white box to better keep user’s attention on the text. </li>
      <li><b>Interaction:</b> Strong focus was put on interaction with the users, by buttons, drop-down menus, selection possibilities, and switching between pages The idea behind is to keep the user interested.</li>
    </ul>


    <h2>
      Discussion
    </h2>

    <h3>
      Overview
    </h3>
    <p> The goal of the overview was to make a user opening our webpage to directly get interested in the subject we visualize. This is done by introducing the user in an abstract and more kind of intuitive way to the data. The use of moving balls seemed perfect for that. This visualisation was based on a project from the Pudding that you can find <a href="https://pudding.cool/2024/11/love-songs/"> here</a>.</p>
    <p>
      Users can navigate through different slides where the balls will group based on their common attributes. By hovering over the different balls, the user can explore which leader each ball represents. If a user would like more information about a leader, clicking on the ball will bring them directly to the search page with extra information about the leader being given. On the last slide, extra information is given about the dataset and what the user can expect from our webpage.
    </p>

    <p>
      The visualization was done using the d3 library force. This makes it possible to make simulations of movement based on certain forces. The forces here were links between leaders having the same attribute of interest. It took a lot of time to find out how this worked. The possibility to do this using hierarchies is mentioned in the documentation, but I was not able to do it like this. Finally I understood how the forceLink worked decided to manually make the links between leaders with the same attribute. The way this is implemented leads to a lot of code redundancy and too much computational power being required. However, due to the dataset being rather limited this does not pose a problem for our project. The biggest issues with the visualisation are: 
    </p>
    <ul>
      <li>Some balls do not join the cluster of their attributes due to being blocked by others. This could be fixed by hardcoding the location of each ball, but this seemed like a step outside the scope of this project.</li>
      <li>Clicking very quickly from one slide to the next might lead to the visualisation not occurring correctly.</li>
      <li>Going from one slide to the next and then back changes the positions of the balls, this is not a big problem it just makes it less consistent. Again, this could be fixed by hardcoding the location of each ball.</li>
    </ul>

    <h3> Charts</h3>

    <p> On this page several graphs were made. Some were made with the idea to explore the data and see the possibilities the dataset had to offer, other were inspired based on the findings of the paper by Acosta et al. (2022). </p>


    <h4>Leadership age versus years in power</h4>

    <p> This graph shows the relationship between the age of the leader and the number of years the leaders stayed in power. A linear regression was plotted to visualize a possible relationship. Depending on the region that is chosen a positive or negative relationship is given. No technical difficulties occurred for the making of this graph.  </p>

    <h4>Education level</h4>

    <p> This is a very simple graph that shows the frequency of each education level across the dataset. A bar chart seemed ideal as this makes it easy to compare the frequency of the different education level, giving an idea of the distribution. Only one technical difficulty was present for this graph. Due to some leaders having empty values for different attributes, the 'groupBy' function of florence DataContainer could not simply be used. To work around this a new datacontainer is simply made containing only the necesarry variables for the making of the graph.  </p>

    <h4>Occupation</h4>

    <p>
     In this bar chart the primary occupation before becoming a rebel leader is visualized in function of the method the rebel leaders used to seize power. By selecting one of the entry methods, the bar chart displays al the leaders that used this entry method to seize power.<br>
     Important to know is that for 20% the occupation is unknown. Therefore, the decision was made to exclude these data from the chart.<br>
     The bar chart was chosen because this chart  is a simple to understand and proportional differences are easily understood. This was done because if a more complex method was chosen, it could have become too complex because of the combination with the entry method variable and the region.<br>
     A point for improvement is that the entry method bar does not go to 100%. There was not enough time to find out what caused this problem.   
   </p>

   <h4>Conflicts and Fatalities</h4>
   
   <p>
    This graph visualizes the duration of conflicts that rebel leaders in the dataset were involved in, in relation to the amount of fatalities that were made by the use of terrorism in that conflict, by each rebel leader's organization.
    <br><br>
    It is meant to give more visual insight into the amount of conflicts with terrorism on the one hand, their respective region of occurrence, and the different amount of terrorism fatalities that have been made by the rebel organization in that conflict. Visual comparison is made possible through this graph to gain better insight into different amounts of terrorism use regarded to the different regions and different lengths of conflicts.
    For example, attention could be put on conflicts with short duration, however with very high fatality numbers.
    <br><br>
    A horizontal bar chart was used and combined with X and Y axis to be able to compare the different variables of amount as height and time as horizontal length. A logarithmic Y-axis was considered regarding the large fatality differences. However, by using such logarithmic scale, only conflicts where enough terrorism fatalities occurred could be included, as the axis only starts at 1. Grid lines were added to be able to better link bars to X and Y values. Colors were evidently added to be able to discern different regions of interest.
    <br>
   </p>

   <h4>Fatalities versus Education Level and Combat Experience</h4>

   <p>
    This graph uses circles with size correlating to number of fatalities made by use of terrorism, that Acosta et al. (2022) added to their database, from research and data of Fortna et al. (2020), compared to the education level and combat experience of rebel leaders. It draws a circle for each combination of Combat Experience (Yes/No) and Education Level (7 levels) that shows the corresponding average amount of fatalities made by the use of terrorism in that category, for a specific region when selected.
    <br><br>
    It is an attempt at visualizing one of the main findings in what was one of the goals of the paper to which this dataset is pertaining, namely the relations between rebel leader characteristics and their actions.
    The researchers of the paper of which this dataset is originating, Acosta et al. (2022) showed correlations between different biographic variables of rebel leaders in the dataset and the use of terrorism in civil war of their organization. They found rebel leaders with a higher education level and previous combat experience to be more likely to avoid the use of terrorism in their conflicts.
    <br><br>
    However, in the graph made in this project, this relationship is visually not directly clear, and thus, not reflecting the conclusions drawn by the Acosta et al. (2022). This can have different possible causes, regarding to the approach used for the fabrication of this graph.
    <br>
    To begin with, the techniques of analysis differ. Acosta et al. (2022) used negative binomial regression models to assess the impact of leaders' characteristics on the fatalities. While in this project, the amount of terrorism usage was simply calculated as a mean, per category of combinations between the education and combat experience. One should thus also look at education and combat experience separately and see if there's a correlation with the paper's conclusions.
    As well should be kept in mind, that taking the mean value is a much less robust technique and explains less. It is very sensitive to outliers in each category, due to which the visualisation may not give an accurate view, combined with that the data distribution can also not be checked to control the accuracy. This could maybe added to give more insight.
    On the other hand, Acosta et al. (2022) also only looked at the relationship for the complete dataset, so our graph might be an indication that their conclusion does not hold for every region separately. This, because their concluded relationship between the both factors and terrorism fatalities is visually best found on our graph only when looking at 'the world' as region.
    <br><br>
    As an extra addition, there could have been thought about the colors that could have been used in a better way to visualize extra information, as in the current version, they only represent the region, which is already selected. There is no direct visual comparison possible between the regions, making the region color coding lose some of its effectiveness.
   </p>

    <h4> Worldmap</h4>

    <p>
      The worldmap can be used to select a region of interest. 
      This can also be done with a simple drop down but the map gives a better idea where this region is and which countries these include.
      The combination of both a map and a drop down menu to select a region is done to be as user-friendly as possible.
      Regions on the worldmap and for the production of graphs were not yet included in the dataset, but were self defined based on the UN region classification, with some minor additional changes for better logical visualization regarding the specific subject.
      The countries assigned to each region, are defined in the ROLE database codebook as the countries to which rebel organizations are fighting, so not the country of origin of the organization or rebel leader. This should be kept in mind for correctly interpreting the different graphs and corresponding data.
    </p>


    <h3> Search</h3>
    <p> In the search page (search.svelte), a search bar is implemented to allow users to look up specific rebel leaders. Users must type at least three characters before a list of possible rebel leaders appears. Once a rebel leader's name is clicked, an information card for that specific rebel leader is displayed. This information card contains all available details about the individual from the ROLE dataset form Acosta et al. (2022), such as the rebel group they led, their ‘also known as’ names, and other characteristics like whether they were married or had children. Additionally, a button is provided that links to Google Images, allowing users to view a picture of the rebel leader. </p>
    <p> It is important to note that this image feature may not always be accurate or reliable, as some rebel leaders have been deceased for a long time or were not widely known. In some cases, individuals with similar names may appear in the search results. Users should approach this feature with caution. However, it was included as an engaging extra element, as it allows users to better visualize the rebel leader in question in most cases. </p>
    <p>The search page is an interesting non-visualization addition to the project, providing a more personal perspective compared to the general data presented in the charts section of the webpage. This feature offers users a deeper, more individualized insight into specific rebel leaders, which can be particularly useful if they are interested in exploring a particular leader in greater detail.</p>
    <p>Most elements from the dataset by Acosta et al. (2022) are included in the search page. However, some details, such as whether a leader studied in the USA or UK or whether they held a religious title, were excluded. These elements were considered less important, especially since they were not applicable to most rebel leaders in the dataset.</p>


    <h3> If there was more time</h3>
    <p> If more time was available for the project, additional graphs and charts could be created to further enhance the visualization of the data. For now, a limited number of graphs and charts have been made that seemed most interesting and relevant to visualize for the research.</p>
    <p>The user-friendliness could also have been improved further, making the site even more accessible.</p>
    <p>There was a plan to also create a conflict webpage if more time had been available. This could have displayed the different conflicts that the studied rebel leaders were involved in, possibly shown on a map by country. However, it was also decided not to include this, as it was not the focus or objective of the paper or the creators of the dataset.</p>
    
    
    <h2> References</h2>
    <p>Acosta, B., Huang, R., & Silverman, D. (2022). Introducing ROLE: A database of rebel leader attributes in armed conflict. Journal of Peace Research, 60(2), 352-361. <a href= https://doi.org/10.1177/00223433221077920>https://doi.org/10.1177/00223433221077920</a></p>
    <p>Fortna, V. P., Lotito, N. J., & Rubin, M. A. (2020). Terrorism in armed conflict: new data attributing terrorism to rebel organizations. Conflict Management And Peace Science, 39(2), 214–236. <a href= https://doi.org/10.1177/0738894220972996>https://doi.org/10.1177/0738894220972996</a></p>
    </div>
    
    <style>
      .text-container{
    max-width: 750px;
    margin: 0 auto;
    padding: 50px;
    text-align: justify;
        /* Box styling: */
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    margin-left: 250px
  }

    </style>