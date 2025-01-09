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
      About of the webpage / Project report
    </h1>

    <h2>
      Introduction
    </h2>
    <p> As part of the Interactive Data Visualization course, a project was created to explore and visualize information about rebel leaders. This study by Acosta et al. (2022) aims to shed light on various aspects of their lives, providing a better understanding of who they are. The aim is to answer key questions such as: Who are they? What drives them? What were their lives like before they became rebel leaders? Do they have children? Wat is the spatial distribution over the world of those rebel leaders? In essence, the goal is with this project to gain deeper insights into the characteristics of rebel leaders around the world and understand them better, all through an interactive and engaging experience. </p>
    <p>The data used in this project is sourced from Acosta et al. (2022), who created a database detailing the attributes of rebel leaders involved in armed conflicts. Because earlier studies about this topic rarely examined whether and how rebel leader characteristics matter for explaining political outcomes, they developed this database. Acosta proposes that the personal backgrounds and experiences of rebel leaders play a crucial role in explaining the behavior of the rebel organizations they lead. The Rebel Organization Leaders (ROLE) database contains a wide range of biographical information on all top rebel leaders in civil wars that occurred between 1980 and 2011. One of the main goals of the paper and the creation of the database is to shift the focus beyond analyzing rebel organizations and campaigns and bring individual leaders more fully into modern conflict and peace studies (Acosta et al., 2022).</p>
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
    <p> The invisible parts (graphs, helpers, data): ???</p> /*is dit nuttig om dit ook op te sommen?*/

    <h2>
      Discussion
    </h2>

    <h3>
      Overview
    </h3>
    <p> The goal of the overview was to make a user opening our webpage to directly get intrested in what we visualize. This is done by introducing the user in an abstract and more kind of intuitive way to the data. The use of moving balls seemed perfect for that. This visualisation was based on a project from the Pudding that you can find <a href="https://pudding.cool/2024/11/love-songs/"> here</a></p>
    <p>
      Users can navigate through different slides where the balls will group based on their common attributes. By hovering over the different balls, the user can see which leader each ball represents. If a user would like more information about a leader, clicking on the ball will bring them directly to the search page with extra information about the leader being given. On the last slide, extra information is given about the dataset and what the user can expect from our webpage.
    </p>

    <p>
      The visualisation was done using the d3 library force. This makes it possible to make simulations of movement based on certain forces. The forces here were links between leaders having the same attribute of intereset. It took a lot of time to find out how this worked. The possibility to do this using hierarchies is mentionned in the documentation, but I was not able to do it like this. Finally I understood how the forceLink worked decided to manually make the links between leaders with the same attribute. The way this is implemented leads to a lot of code redudancy and too much computational power being required. However, due to the dataset being rather limited this does not pose a problem for our project. The biggest issues with the visualisation are: 
    </p>
    <ul>
      <li>Some balls do not join the cluster of their attributes due to being blocked by others. This could be fixed by hardcoding the location of each ball, but this seemed like a step outside the scope of this project</li>
      <li>Clicking very quickly from one slide to the next might lead to the visualisation not occurring correctly</li>
      <li>Going from one slide to the next and then back changes the positions of the balls, this is not a big problem it just makes it less consistent. Again, this could be fixed by hardcoding the location of each ball</li>
    </ul>

    <h3> Charts</h3>

    <p> On this page several graphs were made. Some were made with the idea to explore the data and see the possibilities the dataset had to offer, other were inspired based on the findings of the paper by Acosta et al. (2022) </p>


    <h4>Leadership age versus years in power</h4>

    <p> This graphs shows the relationship between the age of the leader and the number of years the leaders stayed in power. A linear regression was plotted to visualize a possible relationship. Dependig on the region that is chosen a positive or negative relationship is given. No technical difficulties occurred for the making of this graph  </p>

    <h4>Education level</h4>

    <p> This is a very simple graph that shows the frequency of each education level across the dataset. A bar chart seemed ideal as this makes it easy to compare the frequency of the different education level, giving an idea of the distribution. Only one technical difficulty was present for this graph. Due to some leaders having empty values for different attributes, the 'groupBy' function of florence DataContainer could not simply be used. To work around this a new datacontainer is simply made containing only the necesarry variables for the making of the graph.  </p>

    <h4>...</h4>


    <h3> Search</h3>
    <p> In the search page (search.svelte), a search bar is implemented to allow users to look up specific rebel leaders. Users must type at least three characters before a list of possible rebel leaders appears. Once a rebel leader's name is clicked, an information card for that specific rebel leader is displayed. This information card contains all available details about the individual from the ROLE dataset form Acosta et al. (2022), such as the rebel group they led, their ‘also known as’ names, and other characteristics like whether they were married or had children. Additionally, a button is provided that links to Google Images, allowing users to view a picture of the rebel leader. </p>
    <p> It is important to note that this image feature may not always be accurate or reliable, as some rebel leaders have been deceased for a long time or were not widely known. In some cases, individuals with similar names may appear in the search results. Users should approach this feature with caution. However, it was included as an engaging extra element, as it allows users to better visualize the rebel leader in question in most cases. </p>
    
    <h3> If there was more time</h3>
    <p> If more time was available for the project, additional graphs and charts could be created to further enhance the visualization of the data. For now, a limited number of graphs and charts have been made that seemed most interesting and relevant to visualize for the research.</p>
    <p>The user-friendliness could also have been improved further, making the site even more accessible.</p>
    <p>There was a plan to also create a conflict webpage if more time had been available. This could have displayed the different conflicts that the studied rebel leaders were involved in, possibly shown on a map by country. However, it was also decided not to include this, as it was not the focus or objective of the paper or the creators of the dataset.</p>
    
    <h2> Reference</h2>
    <p>Acosta, B., Huang, R., & Silverman, D. (2022). Introducing ROLE: A database of rebel leader attributes in armed conflict. Journal of Peace Research, 60(2), 352-361. <a href= https://doi.org/10.1177/00223433221077920>https://doi.org/10.1177/00223433221077920</a></p>
    
    </div>
    
    <style>
      .text-container{
    max-width: 750px;
    margin: 0 auto;
    padding: 20px;
    text-align: justify;
    }

    </style>