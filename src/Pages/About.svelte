<script>
    let value =''
    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'

    
    $: console.log(value)
    </script>
    <h2>
      Project report
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

    <p> On this page several graphs were made. Some were made with the idea to explore the data and see the possibilities the dataset had to offer, other were inspired based on the findings of the paper by Acosta et al. (2023) </p>

    <h4>Leadership age versus years in power</h4>

    <p> This graphs shows the relationship between the age of the leader and the number of years the leaders stayed in power. A linear regression was plotted to visualize a possible relationship. Dependig on the region that is chosen a positive or negative relationship is given. No technical difficulties occurred for the making of this graph  </p>

    <h4>Education level</h4>

    <p> This is a very simple graph that shows the frequency of each education level across the dataset. A bar chart seemed ideal as this makes it easy to compare the frequency of the different education level, giving an idea of the distribution. Only one technical difficulty was present for this graph. Due to some leaders having empty values for different attributes, the groupBy function of florence DataContainer could not simply be used. To work around this a new datacontainer is simply made containing only the necesarry variables for the making of the graph.  </p>


    <h3> Reference</h3>
    <p>Acosta, B., Huang, R., & Silverman, D. (2023). Introducing ROLE: A database of rebel leader attributes in armed conflict. Journal of Peace Research, 60(2), 352-361. https://doi.org/10.1177/00223433221077920</p>
    <style>

    </style>