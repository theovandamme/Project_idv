<script>
  import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
  import {csvParse, autoType} from 'd3-dsv'
  import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
  import DataContainer from '@snlab/florence-datacontainer'
  import Age_VS_LD from './Graphs/AgeVSLeadershipDuration.svelte'
  import Worldmap from './Pages/Worldmap.svelte'
  import { regressionLinear } from 'd3-regression'
  import ExportCSV from './Helpers/ExportCSV.svelte'
  import Education from './Graphs/Education.svelte'
  import Charts from './Pages/Charts.svelte'
  import Overview from './Pages/overview.svelte'
  import About from './Pages/About.svelte'
  import Search from './Pages/Search.svelte'



  
  // fetch data from CSV to get the raw dataset
  let unique_leaders_raw
  let unique_leaders
  let progress = false
  let leader = ''
  let dataParsed
  
  async function loadCSV (url) {
    const response = await fetch(url)
    const data = await response.text()
    dataParsed = csvParse(data, autoType)
    unique_leaders_raw = new DataContainer(dataParsed)
    progress = true
  }
  loadCSV('Data/unique_leaders.csv');
  
  // make a copy of the raw dataset to use in the different charts


  // selecting the page
  let select_page = 'overview'
  let selected_page = 0

  // opening page selector
  let open = false


  // Making of the selection
 export let selected_region = 'the world'
  let selected_variable = ''
  
  $: if (progress) {
  
    {if (selected_region == 'the world'){
    unique_leaders = unique_leaders_raw
  } else {
    unique_leaders = unique_leaders_raw
                  .filter(row => row.Region === selected_region)
  }}
  }
  // overall settings
  const padding = { left: 80, bottom: 40, top: 5, right: 10 }
  const color = 'rgb(93, 134, 156)'
  

  function open_page_selector() {
        open =! open
  }
  
  // does not work yet
  function download(id) {
        const svg = document.getElementById(id);
        const blob = new Blob([svg.outerHTML], {type: 'image/svg+xml'});
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = `File name ${id}.svg`;
        link.click();
        console.log(svg)
        console.log(svg.outerHTML);
        console.log(blob);
        console.log(link);
    }

</script>

<div class='container'>
{#if (progress)}
<div class='header'>
<h1 class = 'title'>
  ROLE, Rebel Leaders from Around the World
</h1>
</div>

<div class='page_selector' class:page_selector_closed={!open}>

  <div class='page_button' 
  class:page_button_closed={!open}
  class:page_button_selected={selected_page==1 ||select_page=='overview'} 
    on:click={()=>select_page='overview'} 
    on:click={()=>open = false}
    on:mouseenter={() => selected_page = 1} 
    on:mouseleave={() => selected_page = 0}
    >

    <div class= 'page_icon' >
      <img src='./static/overview.svg' 
      width="45" 
      alt='overview_icon'>
    </div>
    {#if (open)}
    <div class= 'page_button_text' ><p> Overview</p>
    </div>
    {/if}
  </div>

  <div class='page_button' 
        class:page_button_closed={!open}
        class:page_button_selected={selected_page==2 ||select_page=='charts'}
        on:click={()=>select_page='charts'}
        on:click={()=>open = false}
        on:mouseenter={() => selected_page = 2} 
        on:mouseleave={() => selected_page = 0}>
    <div class= 'page_icon'>
      <img src='./static/Charts.svg' 
      width="45"
      alt='charts_icon' >
    </div>
    {#if (open)}
    <div class= 'page_button_text'><p> Charts</p></div>
    {/if}
  </div>

  <div class='page_button' class:page_button_selected={selected_page==3 ||select_page=='conflicts'}
        class:page_button_closed={!open}
        on:click={()=>select_page='conflicts'}
        on:click={()=>open = false}
        on:mouseenter={() => selected_page = 3} 
        on:mouseleave={() => selected_page = 0}>

    <div class= 'page_icon'>
      
      <img src='./static/Conflicts.svg' 
      width="45" 
      alt='conflicts_icon'>
    </div>
    {#if (open)}
    <div class= 'page_button_text'><p> Conflicts</p></div>
    {/if}
  </div>

  <div class='page_button' 
        class:page_button_closed={!open}
        class:page_button_selected={selected_page==4 ||select_page=='search'}
        on:click={()=>select_page='search'}
        on:click={()=>open = false}
        on:mouseenter={() => selected_page = 4} 
        on:mouseleave={() => selected_page = 0}>
    <div class= 'page_icon'>
      <img src='./static/search.svg' 
      width="45"
      alt='charts_icon' >
    </div>
    {#if (open)}
    <div class= 'page_button_text'><p> Search</p></div>
    {/if}
  </div>
  
  <div class='page_button' 
        class:page_button_closed={!open}
        class:page_button_selected={selected_page==5 ||select_page=='about'}
        on:click={()=>select_page='about'}
        on:click={()=>open = false}
        on:mouseenter={() => selected_page = 5} 
        on:mouseleave={() => selected_page = 0}>
    <div class= 'page_icon'>
      <img src='./static/about.svg' 
      width="45"
      alt='charts_icon' >
    </div>
    {#if (open)}
    <div class= 'page_button_text'><p> About</p></div>
    {/if}
  </div>
  
  <div class='double_arrow_open' class:double_arrow_closed={!open} on:click={open_page_selector}>
  <img 
      src='./static/double_arrow.svg'   
      alt='double_arrow' 
      class='double_arrow'
      class:double_arrow_icon_closed={!open}
      >
  </div>
</div>
  <div class='contents'>
  {#if (select_page=='overview')}
    
    <Overview
    unique_leaders={unique_leaders}
    unique_leaders_raw={unique_leaders_raw}
    progress={progress}
    raw_data = {dataParsed}
    bind:select_page={select_page}
    bind:leader={leader}/>
  {:else if (select_page=='charts')}
    <Charts
    unique_leaders={unique_leaders}
    unique_leaders_raw={unique_leaders_raw}
    progress={progress}
    bind:selected_region={selected_region}/>
    {:else if (select_page=='conflicts')}
    <h1>
      This feature is not yet available
    </h1>
    {:else if (select_page=='search')}
    <Search
    DC={unique_leaders}
    Clickedleader={leader}/>
    {:else if (select_page=='about')}
      <About/>
  {/if}
  </div>
  


  {/if}
</div>
<style>
.container{width:101.4%;
          min-width: 1000px;
            margin-left: -10px;
            margin-top: -10px;
            }
.header{width:99.4%;
  height: 80px;
  line-height: 80px;
  padding-left: 20px;
  border-bottom-style: solid;
  border-width: 1px;
  border-color:#116466;
  z-index:9999;
  position:fixed;
  background-color: #ebebeb;
  }
.title{ min-width: 950px;
  height: 30px;}
.page_selector{width:120px;
  float:left;
  padding-left: 20px;
  height: 1100px;
  border-right-style: solid;
  border-width: 1px;
  border-color:#116466;
  z-index:9998;
  position:fixed;
  background: fixed #ebebeb;
  top:79px;
}
.page_selector_closed{width: 60px;
    }
.page_button {width: 140px;
              height: 65px;
              margin-left: -20px;
              margin-top: -18px;
              cursor:pointer;}
.page_button_closed {width: 80px;
              height: 65px;
              margin-left: -20px;
              margin-top: 0px;

}
.page_button_selected{
                      background-color: lightgray;
                      border-right-style: solid;
                      border-width: 1px;
                      border-color:#116466;}
.page_icon{margin-left: 10px;
          padding-top: 4px;
          float: left;}
.page_button_text{line-height: 65px;
                  font-size: 18px;
                  margin-left: 60px;}
.double_arrow_open{position: fixed;
                    margin-left: 108px;
                    margin-top: -183px;
                  background-color: #9fc1b8;
                  cursor:pointer;}    
.double_arrow_closed{position: fixed;
                    margin-left:47px;
                    margin-top: -183px;
                  background-color: #9fc1b8;} 

.double_arrow{width: 25px;
              margin-top: 3px;
              transform: rotate(180deg);
              }   
.double_arrow_icon_closed{width: 25px;
                margin-top: 3px;
                transform: rotate(0deg)}     
.contents{
  width:90%;
  padding:100px;
}
:global(body){
  background-color:#ebebeb;
  color:#116466;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

</style>