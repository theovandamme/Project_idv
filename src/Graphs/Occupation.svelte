<script>
import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis, x2s } from '@snlab/florence'
import { regressionLinear } from 'd3-regression'
import { schemeSpectral,interpolateSpectral,interpolatePuOr } from 'd3-scale-chromatic';
import { scaleLinear, scaleBand, scaleTime, scaleOrdinal } from 'd3-scale'
import DataContainer from '@snlab/florence-datacontainer'
export let DC_raw // Store parsed data
export let selected_region
export let width


let leaders_occupation // Store data grouped by occupation
let x1_entry = [] // Store x1 values for the entry method chart
let x2_entry = [] // Store x2 values for the entry method chart
let scaleX,scaleY,scaleColor_occupation,scaleColor_entryMethod // x scale for the occupation chart
let selectedEntryMethod = "All" // the default selected entrymethod is empty
let showAbout = false; // in default the About content is not shown
let entryMethod_container
let done = false // Flag to indicate when data is fully loaded and ready
let isHovering = false
let hoveredEntryMethod = "Hover over a bars to see details"; // Default message
let hoveredX2Entry = null;
let correct_DC = true

$: console.log(correct_DC)
function toggleAbout() { 
    showAbout = !showAbout;
  }

function defineScalecolor_occ(domain) {
    return scaleOrdinal()
        .domain(domain)
        .range(
            Array.from({ length: domain.length }, (_, i) =>
            interpolateSpectral(i / (domain.length - 1))
            )
        );
}

function defineScalecolor_entry(domain) {
    return scaleOrdinal()
        .domain(domain)
        .range(
            Array.from({ length: domain.length }, (_, i) =>
            interpolatePuOr(i / (domain.length - 1))
            )
        );
}

function handleMouseover(event, d) {
    hoveredEntryMethod = 'This should change in the entry method and the percentage';
    hoveredX2Entry = d.x2_entry;
    isHovering = true;
  }

  function handleMouseout(event) {
    hoveredEntryMethod = "Hover over a bar to see details";
    hoveredX2Entry = null;
    isHovering = false;
  }
function updateOccupationData() {
    // Use the full dataset if no EntryMethod is selected
    let filteredLeaders
    if (selectedEntryMethod=='All'){
        filteredLeaders = DC_raw
    } else {
        filteredLeaders = DC_raw.filter(row => row.entrymethod === selectedEntryMethod)
    }
    correct_DC = false
    if (filteredLeaders.columnIsValid('occupation') ){
    let new_filteredLeaders = new DataContainer ({occupation: filteredLeaders.column('occupation'), leadercode: filteredLeaders.column('leadercode') })
    correct_DC = true
    // Group by occupation and summarize total counts
    leaders_occupation = new_filteredLeaders.dropNA()
        .groupBy("occupation")
        .summarise({ total_count: { leadercode: "count" } });
    // Update scales
    scaleX = scaleBand()
        .domain(leaders_occupation.domain("occupation"))
        .paddingInner(0.3);
    scaleY = scaleLinear()
        .domain([0, leaders_occupation.domain("total_count")[1]])
        .range([0, 300]);
    // Update color scale
    }
}

function DefinePercentages(leaders) {
    const entryMethod = leaders.domain('entrymethod') // Get the unique entry methods used by the leaders
    let numberOfLeaders = leaders.nrow(); // Get the total number of leaders
    let x1_entry_local = [0] // Start x1_entry with 0 (for cumulative percentages)
    let x2_entry_local = [] // Store the second set of x values
    let percentage = 0 // Initialize percentage to 0
    entryMethod_container = new DataContainer({entryMethod})

    // // Loop through each entry method to calculate the cumulative percentage for each method
    for (let i = 0; i < entryMethod.length; i++) {
        let method = entryMethod[i]; // Current entry method
        let count = leaders.filter(row => row.entrymethod === method).nrow(); // Get the count of leaders with this entry method
        percentage += (count / numberOfLeaders) * 100 ; // Calculate the percentage of total leaders using this method
        x1_entry_local.push(percentage); // Append the cumulative percentage to x1_entry_local
        x2_entry_local.push(percentage);
         // Append the current percentage to x2_entry_local
    }
    x1_entry_local.pop();  // Remove the last entry from x1_entry_local (as per original code logic)
    entryMethod_container.addColumn('x1_entry', x1_entry_local)
    entryMethod_container.addColumn('x2_entry', x2_entry_local)

  return { entryMethod_container }
}

updateOccupationData()
scaleColor_entryMethod = defineScalecolor_entry(DC_raw.domain('entrymethod'))
if (correct_DC){
    scaleColor_occupation = defineScalecolor_occ(leaders_occupation.domain("occupation"));
}

DefinePercentages(DC_raw)

$: if (selected_region){
    selectedEntryMethod='All'

}
$: if (selectedEntryMethod) {
    updateOccupationData();
    DefinePercentages(DC_raw)
}
</script>
<div class="title">
    <!-- title/header content goes here -->

    
    <label for="entry-select">Choose an entry method:</label>

    <select bind:value={selectedEntryMethod} name="EntryMethods" id="entry-select">
    <option value="All">All</option>
    {#each DC_raw.domain('entrymethod') as method}
    <option value={method}>{method}</option>
    {/each}
  </select>
  </div>
    {#if (correct_DC)}
    <Graphic width={width} height={650} {scaleX} {scaleY} flipY padding={{left: 40, right:10, top: 25, bottom: 40}}>
        <RectangleLayer 
        x1={leaders_occupation.column('occupation')} 
        x2={x2s(leaders_occupation.column('occupation'))} 
        y1={leaders_occupation.map('total_count', x => 0)}
        y2={leaders_occupation.column('total_count')} 
        keys={leaders_occupation.column('occupation')}
        fill={leaders_occupation.column('occupation').map(scaleColor_occupation)}
        />

        <XAxis title="Occupation" labelRotate=75 labelOffset=5 labelFontSize=7 tickSize=11/> X axis with rotated labels
        <YAxis title='Count'/> 
    </Graphic>
    {/if}
    <Graphic 
    width={width} height={100} backgroundColor={'blue'} scaleX= {scaleLinear().domain([0,100])} > 

        <RectangleLayer 
          x1={entryMethod_container.column('x1_entry')} 
          x2={entryMethod_container.column('x2_entry')} 
          y1={entryMethod_container.column('x1_entry').map((x) =>x= 0)} 
          y2={entryMethod_container.column('x1_entry').map((x) =>x= 1)}
          fill={entryMethod_container.column('x2_entry').map(scaleColor_entryMethod)}
          onMouseover={(event, d) => handleMouseover(event, entryMethod_container)} 
          onMouseout={handleMouseout}
          />  
          <XAxis/>
      </Graphic> 
<style>
</style>