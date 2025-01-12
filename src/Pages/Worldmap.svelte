<script>
  import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis, PolygonLayer, fitScales,Label} from '@snlab/florence';
  import { regressionLinear } from 'd3-regression';
  import { scaleLinear, scaleBand, scaleTime, scaleOrdinal } from 'd3-scale';
  import { schemePaired,schemeSet3 } from 'd3-scale-chromatic';
  import DataContainer from '@snlab/florence-datacontainer';
  import { WorldRegions } from '/src/Helpers/WorldRegionExport.js';
  import color_region from '/src/Graphs/Overview_graph.svelte'
  import { color } from 'd3-color'
 export  let selected_region = 'the world'

 let darkenedSchemeSet3 = schemeSet3.map(c => color(c).darker(0.7).toString())

  const WRegions = new DataContainer(WorldRegions);
  WRegions.setKey('COUNTRY') // set the key to the specific country
  console.log("Loaded Data:", WRegions);

  // set up scales
  const myGeoScale = fitScales(WRegions.domain('$geometry')); // 1. position
  const myColorScale = scaleOrdinal() // 2. fill color
    .domain(WRegions.domain('region').sort((a, b) => a.localeCompare(b)))
    .range(darkenedSchemeSet3);
    

    
  // 3. Mouseover behavior
  let hover = false;
  let key
  let RegionData

  $: Region = hover ? (WRegions.row({key:key}))['region'] : 'the world'
  $: RegionData=WRegions.filter(row=>row.region === selected_region)

  //  $: console.log(RegionData)
  

function handleMouseover(event) {
  hover = true
  key= event.key; // Update the active key
}
 function handleMouseout() {
    hover = false // Reset active
  }

  // 4. handle clicks

  let click = false
function handleClick(event){
    click = event.key
  } 
  $:clickedRegion = click ? (WRegions.row({key:click}))['region'] : 'the world'

 $:if (click && (clickedRegion !== 'Antarctica' && clickedRegion !== 'East Asia')) {
    selected_region = clickedRegion;
} else {
    selected_region = 'the world';
}
$:console.log('the selected region:',selected_region)


</script>

  <div class="main-chart">
    <Graphic width={500} height={200} backgroundColor={'blue'} {...myGeoScale}
      flipY>
      <PolygonLayer
        geometry={WRegions.column('$geometry')}
        stroke={'white'}
        strokeWidth={1}
        fill={WRegions.map('region', myColorScale)}
        keys={WRegions.column('COUNTRY')}
        onTouchdown={handleMouseover}
        onMouseout={handleMouseout}
        onClick={handleClick}
      />
      <!-- to add a red polygon from the selected region on top  -->
      {#if click !== false}
      <PolygonLayer
      geometry={RegionData.column('$geometry')}
      strokeWidth={5}
      fill={'red'} />  
          
      {/if}
     </Graphic>
    </div>
  {#if hover == true}
    <div>
    <p> {Region}</p>
  </div>
  {/if}

<style>
  .graph {
    font-family: Arial, sans-serif;
  }
  .main-chart{
    position:absolute;
  }
  p {
    position:absolute;
    top: 20px;

    left: 1050px;
    background: white;
    padding: 5px 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    pointer-events:fill;
  }
</style>
