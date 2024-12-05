<script>

    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    import Age_VS_LD from '../Graphs/AgeVSLeadershipDuration.svelte'
    import Worldmap from './Worldmap.svelte'
    import ExportCSV from '../Helpers/ExportCSV.svelte'
    import Education from '../Graphs/Education.svelte'
    import ExportSvg from '../Helpers/ExportSVG.svelte'
    import FatalConflict from '../Graphs/FatalConflict.svelte'
    import Occupation from '../Graphs/Occupation.svelte'
    export let unique_leaders_raw
    export let progress
    export let unique_leaders

    let divElement
    let width, height
    
    let selected_region = 'the world'
    let selected_variable = ''
    $: if (progress) {

    {if (selected_region == 'the world'){
    unique_leaders = unique_leaders_raw
    } else {
    unique_leaders = unique_leaders_raw
                  .filter(row => row.Region === selected_region)
  }}
  }
  $: if (selected_variable){
    selected_region='the world'
  }

  // the div element where i use divElement is graph_and_description
  $: if (selected_variable !==''){console.log(divElement)}
    // this works fine 
  // $: console.log(divElement.querySelectorAll('svg')) // this doesn't
  // overall settings
  const padding = { left: 80, bottom: 40, top: 5, right: 10 }
  const color = 'rgb(93, 134, 156)'

    </script>
      <div  id='chart_page' class = 'page' >

        <div class = 'graph1' bind:clientWidth={width} bind:clientHeight={height}>
          <h2 class = 'charts'>Charts</h2>

          <p class = 'charts'>Please select the data you would like to visualize</p>

          <select bind:value={selected_variable} class='selector sel1'>
            <option value=''> --Choose an option</option>
            <option value= 'LeadAge_VS_YIP' >Leadership age versus years in power</option>
            <option value= 'Education' >Education level</option>
            <option value= 'FatalConflicts' >Fatality and duration of conflicts</option>
            <option value= 'Leader_occupation' >Leaders occupation</option>
          </select>

          <p class = 'charts'>And the region of interest</p>
          <select bind:value={selected_region} name ="provinces" id='select_provinces' class='selector sel2'>
            <option value='the world'> The world</option>
            {#each unique_leaders_raw.domain('Region').filter(val => val !=='Oceania') as item}
            <option value={item}> {item}</option>
            {/each}
          </select>

          <div bind:this={divElement} class= 'graph_and_description' >
          {#if (selected_variable == 'LeadAge_VS_YIP')}
         
          <Age_VS_LD
          DC_raw = {unique_leaders}
          width = {width}
          region = {selected_region}/>
          {:else if (selected_variable=='Education')}
          <Education
          DC_raw = {unique_leaders}
          width = {width}/>
          {:else if (selected_variable=='FatalConflicts')}
          <FatalConflict 
          width = {width}
          DC_raw={unique_leaders}/>
          {:else if (selected_variable=='Leader_occupation')}
          <Occupation 
          width={width}
          selected_region={selected_region}
          DC_raw={unique_leaders}/>
          {/if}

          </div>
          <div class = "export">
          <ExportCSV
          DC_raw = {unique_leaders}
          selected_region = {selected_region}/>
          <ExportSvg
          />
          
          </div>
        </div>


      </div>
    

    <style>

.page {width:85.3%;
        
          height:740px;
          float:left;
        }
.charts {margin-left: 20px;
        margin-bottom: 10px;
        margin-top: 10px;
        }
.selector{width: 100%;
                  height: 30px;
                  margin-left:20px;
                  cursor:pointer;}

.sel2{margin-top: -50px;
      margin-bottom: 10px;
    }
.graph1 {width:100%;
          
          height:940px;
          float:left;
          position: relative;
          color:#116466;}
.graph_and_description { height:900px;
                        padding-left: 20px;

      }          
.export {margin-top: -30px;}
    </style>