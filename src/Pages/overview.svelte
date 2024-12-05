<script>

    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    export let unique_leaders_raw
    export let progress
    export let unique_leaders
    let width, height

</script>
    <div class= 'page'>
        <h2>
          Overview
        </h2>
        
        <div class = worldmap>
          <p> The dataset we are using for our project is the Rebel Organization Leaders database. This database consists of information about top rebel leader such as the way they came into power, their education, personnal information etc. The dataset consists of a table with categorical, ordinal and quantitative data. The main goal is for the user to be able to analyze and search. Analyze will happen mostly in the charts section. Here the different visualizations can be used to discover new information by observing the data. It will also possibly to record visualizations as artifacts thanks to the export chart button (not yet working). Search will mostly happen in another tab where it will be possible to search for a specific leader (by name or attributes). </p>
          <p>The first graph, leadership age versus years in power is a combination of point and line marks. The used magnitude channel is a position on a common scale and no identiy channel was used. This graph was made to observe the link between both variables. The linear regression shows some unexpected behavior, but is never relevant enough. It it thus a visualization with little information gain that does not neceserally need to be in the final project. The second graph shows the frequency (# of times) of the different education levels that were achieved by the rebel leaders. A barchart was used because it makes it visually easy to compare the different education levels. For both graphs the user can filter the data by selecting it based on the world regions. These world regions are now abstract but will be visually represented in the map in the overview. The data of the selected region can also be downloaden using the button under the graph. </p>

          <p> Other interactions are already possible, like browsing from one page to another. However only the Charts page is already more worked out, the other pages will be for later in the project. </p>

          <p> Questions and remarks
          </p>
          <ul>
            <li>I'm selecting a Div by using bind:this=divElement. When i console.log() my divElement it shows the correct structure and div that i want. The Div contains an svg and i wanted to acces that using divElement.querySelectorAll('svg'). When i log this in my console it returns an empty nodeList. Should i use something else to select my svg? This is done in my Charts.svlete</li>
            <li>I have event handler on div's in my app.svelte. Several warnings occur when i do this, i haven't had the time to look at them and what they mean. </li>
            <li>
              The education graph returns errors due to the path for some of the regions, this does not block anything. 
            </li>
            <li>
              The double-arrow to open and close the page selector is not yet optimal, sometimes a click on it will not do the action. Issue to be fixed
            </li>
          </ul>
          
        </div>
    </div>
<style>
    h2 {padding-left: 20px;}
    .page {width:85%;
            float: left;
          height:740px;
        }
    .worldmap {width:100%;
        height:700px;
        position: relative;
        float:left;
        padding-left: 20px;}
</style>