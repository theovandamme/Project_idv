<script>
  import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis, PolygonLayer, fitScales,Label} from '@snlab/florence';
  import { regressionLinear } from 'd3-regression';
  import { scaleLinear, scaleBand, scaleTime, scaleOrdinal } from 'd3-scale';
  import { schemePaired,schemeSet3 } from 'd3-scale-chromatic';
  import DataContainer from '@snlab/florence-datacontainer';
  import { WorldRegions } from '/src/Helpers/WorldRegionExport.js';
  import color_region from '/src/Graphs/Overview_graph.svelte'



  const WRegions = new DataContainer(WorldRegions);
  WRegions.setKey('COUNTRY') // set the key to the specific country
  console.log("Loaded Data:", WRegions);

  // set up scales
  const myGeoScale = fitScales(WRegions.domain('$geometry')); // 1. position
  const myColorScale = scaleOrdinal() // 2. fill color
    .domain(WRegions.domain('region'))
    .range(schemeSet3);
    // const myColorScale = scaleOrdinal().domain(WRegions.domain('region'))
    //   .range(color_region)

    
  // 3. Mouseover behavior
  let active = '';
  let RegionData
  $: Region = active ? (WRegions.row({key:active}))['region'] : 'the world'
  // $:if (active !== ''){
  //   RegionData=WRegions.filter(row=>row.region === Region)
  //   console.log(RegionData)
  // } else {
  //   RegionData = WRegions
  // }

  // $: Region =(WRegions.row({key:active}))['region'] 
  $: RegionData=WRegions.filter(row=>row.region === Region)
   $: console.log(RegionData)
  

function handleMouseover(event) {
  active = event.key; // Update the active key
}
  function handleMouseout() {
    active = '' // Reset active
    // console.log("Mouseout: Active Key Reset");
  }

  /////// handle clicks

  let selected_region = 'the world'
  let click = false
$:console.log('the selected region:',selected_region)
  function handleClick(){
  click = true
}
 $:if (click){
    selected_region=Region
  }else{
    selected_region='the world'
  }
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
        onMouseover={handleMouseover}
        onMouseout={handleMouseout}
        onClick={handleClick}
      />
      <!-- trying to add the selected region on top  -->
      {#if active !== ''}
      <PolygonLayer
      geometry={RegionData.column('$geometry')}
      strokeWidth={5}
      fill={'red'} />  
          
      {/if}
     </Graphic>
    </div>
  {#if active !== ''}
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
