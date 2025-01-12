<!-- I already abstracted this graph in a separate Svelte component
 to ease further coding when working as a group
 Changes will of course still have to be made, 
 especially to the dimensions of the used Sections,
 and also just because not every element of this assignment
 will be present in the final web page,
 but I considered it being a good starting point -->

 <script>
    import { scaleLinear, scaleOrdinal, scaleLog } from 'd3-scale'
    import { Section, RectangleLayer, XAxis, YAxis, YGridLines, XGridLines, DiscreteLegend, Label, Graphic} from '@snlab/florence'
    import DataContainer from '@snlab/florence-datacontainer'
    import { schemeSet3 } from 'd3-scale-chromatic'
    import { color } from 'd3-color'


    export let DC_raw
    export let width
    export let darkenedSchemeSet3


    
    // export let selectedReligion
    
    let unique_leaders_yap
    let regionColorScale
    let scaleX
    let scaleY
    let padding
    let selectedIndex = null
    let selected_page = 0
    

    
        const thicknessFactor = 1.15; // to control thickness of bars, as I'm using a log scale


        $: unique_leaders_yap = DC_raw.mutate({
            x1: r => r.ldrstwar_year,
            x2: r => r.ldrendwar_year,
            y1: r => r.km_a,
            y2: r => r.km_a * thicknessFactor
        });

        $: unique_leaders_yap = unique_leaders_yap.filter(
            row => row.km_a > 0 && !isNaN(row.km_a)
        )


        $: uniqueRegions = [...new Set(unique_leaders_yap.column('Region'))];

        $: domainX = [
            unique_leaders_yap.min('ldrstwar_year'),
            unique_leaders_yap.max('ldrendwar_year'),
            ];

        $: domainY = [1, unique_leaders_yap.max('km_a')+1500];

        $: scaleX = scaleLinear().domain(domainX).range([0, 800]);
        $: scaleY = scaleLog().domain(domainY).range([400, 0]);

        // Create colour scale

        regionColorScale = scaleOrdinal()
            .domain(DC_raw.domain('Region').sort((a, b) => a.localeCompare(b)))
            .range(darkenedSchemeSet3);


        

        // function handleMouseClick (event) {
        //     console.log(event)
        //     selected_region = event.key
        // }
        // function handleMouseClickElse (event) {
        //     selected_region = ''
        // }
        

padding = { left: 50, bottom: 40, top: 10, right: 10 }

</script>

<h4>Fatalities Made by Terrorism & Duration of Conflict</h4>
{#if selectedIndex == null}
 <p>Hover over a bar to see rebel leader involved...</p>
{:else if selectedIndex !== null}

  <div>
    <p>Rebel leader: <b style="color: red">{unique_leaders_yap.column('fullbirthname')[selectedIndex]}</b></p>
  </div>
{/if}

<p>Look up the name of the rebel leader in our database search tool on the site, to expand your knowledge.</p>

<!-- The zoom function for the RectangleLayer crashes by certain input.
 I couldn't figure how to fix it yet. -->
 <Graphic width={width} height={550}>   
 <Section
    x1={0.82}
    x2={1}
    y1={0}
    y2={1}
    {padding}
      
>
<!-- Legend for the RectangleLayer -->
    <DiscreteLegend
        xDivider={0.2}
        yDivider={0.1}
        x1={0} x2={1}
        y1={0} y2={1}
        fill={regionColorScale.range()}
        labels={regionColorScale.domain()}
        labelFont = "Courier"
        labelFontSize = {10}
        opacity = {0.5}
        stroke=grey
    >
        <Label x={0} y={0.05} text="Legend" anchorPoint=lb fontFamily = "Courier" fontSize=24 fontWeight=800 />

    </DiscreteLegend>
</Section>
<Section
    x1={0}
    x2={0.85}
    y1={0}
    y2={1}
    {scaleX}
    {scaleY}
    {padding}
    flipY
    zoomable
    pannable
    
    >
    <RectangleLayer
        x1={unique_leaders_yap.column('x1')}
        x2={unique_leaders_yap.column('x2')}
        y1={unique_leaders_yap.column('y1')}
        y2={unique_leaders_yap.column('y2')}
        fill={unique_leaders_yap.map('Region', r => regionColorScale(r))}
        opacity = {0.6}
        stroke={({ index }) => (index === selectedIndex ? "red" : "grey")}
        onMouseover={({index}) => (selectedIndex = index)}
        onMouseout={() => (selectedIndex = null)}


        />
    <XAxis 
        tickCount = {10} 
        labelFormat={d => d} 
        baseLine={false}
        labelRotate = {0.4} 
        labelFont = "Courier" 
        title="Duration of Conflict" 
        titleFont="Courier" 
        titleYOffset={30}
        /> 
    <YAxis 
        tickCount = {4} 
        labelFormat={d => d} 
        baseLine={false}
        labelRotate = {0.4} 
        labelFontSize = {8} 
        labelFont = "Courier"
        title="Annual Terrorist Fatalities Made" 
        titleFont="Courier" 
        titleXOffset={-30} 
        />
        
    <YGridLines opacity = {0.2} count = {20}/>
    <XGridLines opacity = {0.15} count = {50} />

</Section>

</Graphic>

<h4>About the graph:</h4>
<p style='text-align: justify; width: 75%'>This graph combines data about rebel leader characteristics and the actions of the rebel organization they lead.
     In this case the annual amount of fatalities made by the organization through the use of terrorism is visualized compared with the length of the conflict they were involved in.
    The colors visualize the region of the country against which the rebel organization was fighting.
<br>
For interpretation, caution should be paid that if there is only 1 terrorist event in a 10-year conflict, the number of annual deaths from terrorism shown on the graph will obviously be equal to the number of deaths in that one year divided by ten.
</p>
<!-- <h1 style="color: blue;">
  {selectedIndex === null ? "None selected" : unique_leaders_yap.column('fullbirthname')[selectedIndex]}
</h1> -->
<!-- <div class="about">
    <p>This graph displays the duration of different rebel leaders' conflicts in time and 
      their respective amount of generated fatalities by terrorism.
      This chart is meant to give better insight in the amount of conflicts on the one hand, and the different amount of terrorism fatalities between world regions
      and as well relative to the length of a certain conflict.
      <br>Further interaction with the graph and further exploring is possible by zooming in, and could be done by adding tooltips when hovering over each bar,
      to give information about the characteristics of the rebel leader in each conflict, but this is not implemented yet.
      <br><br>
      A horizontal bar chart graph was chosen to best visualize the time character of the subject of this graph, as well as the quantitative aspect of terrorist fatalities and color coding for each region
      where added for better visual interpretation. A logarithmic Y-axis was considered regarding the large fatality differences. The ultimate purpose of this kind of graph is mainly to identify further
      subjects of interest. The approach used can be framed within Munzner's What/Why/How three-part analysis framework for data visualization.

    </p>
  </div> -->

<style>
    .page_button {width: 140px;
              height: 65px;
              margin-left: -20px;
              margin-top: -18px;
              cursor:pointer;}
</style>