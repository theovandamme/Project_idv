<script>
    export let DC
    export let Clickedleader 
    let items = DC.domain('fullbirthname')
    let leader 

    if (Clickedleader !== ''){
      leader = DC.filter(row => row.fullbirthname === Clickedleader)
    }
    import {
      Page,
      Navbar,
      Searchbar,
    } from 'konsta/svelte';
  
    let searchQuery = '';

  
    function handleSearch(e) {
      searchQuery = e.target.value;
    }
  
    function handleClear() {
      searchQuery = '';
    }

    function selectLeader(item){
        leader = DC.filter(row => row.fullbirthname === item)
        handleClear
        console.log(leader)
    }

    $: possibleItems = items.filter((item)=>item.toLowerCase().includes(searchQuery.toLowerCase()))

  </script>
  
  <Page>
    <div class='search'>
    <Navbar title="Search rebel leader">
      <Searchbar
        slot="subnavbar"
        onInput={handleSearch}
        value={searchQuery}
        onClear={handleClear}
        placeholder="Type at least 3 characters"
      />
    </Navbar>

      {#if searchQuery.length >= 3}
        {#if possibleItems.length === 0}
          <button>No result found</button>
        {/if}
        {#each possibleItems as item (item)}
         <button on:click={()=>{selectLeader(item), handleClear()}}> {item}</button>
        {/each}
      {/if}
    </div>

    
    {#if leader}
      <div class = "container"> 

      <h1>{leader.column('fullbirthname')}</h1>
    
      <a class="image-button" href="https://www.google.com/search?q={leader.column('fullbirthname')}+rebel+leader&tbm=isch" target="_blank">View picture of {leader.column('fullbirthname')}
        <span class="image-caption">Link to Google Images, sometimes it is possible that the pictures don't correspond with the rebel leaders</span>
      </a>
     
      <p><b>Leader of rebelgroup:</b> {leader.column('groupname')}</p>
      {#if !(String(leader.column('popularname')) == String(leader.column('fullbirthname')))}
        <p><b>Better known as:</b> <i> {leader.column('popularname')}</i></p>
      {:else}
        <p><b>Better known as:</b> No alternate name known</p>
      {/if}  
      <p><b> Gender:</b> {leader.column('gender')}</p>
      <p><b>Born in:</b> {leader.column('yearofbirth')}</p>
      {#if leader.column('yearofdeath') != '' || leader.column('deathcause') != ''}
        <p><b>Died in:</b> {leader.column('yearofdeath')}</p>
        <p><b>Deathcause:</b> {leader.column('deathcause')}</p>
      {:else}
        <p><b>Still alive</b></p>
      {/if}

      <p><b>Born in:</b> {leader.column('placeofbirth')}</p>
      <p><b>Conflict involved:</b> {leader.column('confdesc')}</p>
      <p><b>Fighting against:</b> {leader.column('stname')}</p>
      <p><b>Leadership age:</b> {leader.column('leadershipage')}</p>
      <p><b>Entry method as leader:</b> {leader.column('entrymethod')}</p>
      <p><b>Level of education achieved:</b> {leader.column('education')}</p>
      <p><b>Occupation category before rebel leader:</b> {leader.column('occupation')}</p>
      <p><b>Religion:</b> {leader.column('religion')}</p>

      
      {#if leader.column('married') == 1}
      <p><b>Married:</b> Yes</p>
      {:else if leader.column('married') == 0}
      <p><b>Married:</b> No</p>
      {:else}
       <p><b>Married:</b> No data available</p>
      {/if}

      {#if leader.column('children') == 1}
      <p><b>Any children:</b> Yes</p>
      {:else if leader.column('married') == 0}
      <p><b>Any children:</b> No</p>
      {:else}
       <p><b>Any children:</b> No data available</p>
      {/if}
      
      {#if leader.column('military') == 1}
      <p><b>Military experience before rebel leader:</b> Yes</p>
      {:else if leader.column('military') == 0}
      <p><b>Military experience before rebel leader:</b> No</p>
      {:else}
       <p><b>Military experience before rebel leader:</b> No data available</p>
      {/if}

      {#if leader.column('combat') == 1}
      <p><b>Previous combat experience before becoming rebel leader:</b> Yes</p>
      {:else if leader.column('combat') == 0}
      <p><b>Previous combat experience before becoming rebel leader:</b> No</p>
      {:else}
       <p><b>Previous combat experience before becoming rebel leader:</b> No data available</p>
      {/if}

      {#if leader.column('govpost') == 1}
      <p><b>Government post before becoming rebel leader:</b> Yes</p>
      {:else if leader.column('govpost') == 0}
      <p><b>Government post before becoming rebel leader:</b> No</p>
      {:else}
       <p><b>Government post before becoming rebel leader:</b> No data available</p>
      {/if}

      {#if leader.column('exile') == 1}
      <p><b>Been in exile before becoming rebel leader:</b> Yes</p>
      {:else if leader.column('exile') == 0}
      <p><b>Been in exile before becoming rebel leader:</b> No</p>
      {:else}
       <p><b>Been in exile before becoming rebel leader:</b> No data available</p>
      {/if}

      {#if leader.column('studyab') == 1}
      <p><b>Studied abroad before becoming rebel leader:</b> Yes</p>
      {:else if leader.column('studyab') == 0}
      <p><b>Studied abroad before becoming rebel leader:</b> No</p>
      {:else}
       <p><b>Studied abroad before becoming rebel leader:</b> No data available</p>
      {/if}

      {#if leader.column('workab') == 1}
      <p><b>Worked abroad before becoming rebel leader:</b> Yes</p>
      {:else if leader.column('workab') == 0}
      <p><b>Worked abroad before becoming rebel leader:</b> No</p>
      {:else}
       <p><b>Worked abroad before becoming rebel leader:</b> No data available</p>
      {/if}

      {#if leader.column('prison') == 1}
      <p><b>Imprisoned before becoming rebel leader:</b> Yes</p>
      {:else if leader.column('prison') == 0}
      <p><b>Imprisoned before becoming rebel leader:</b> No</p>
      {:else}
       <p><b>Imprisoned before becoming rebel leader:</b> No data available</p>
      {/if}

      <p><b>For more info about the rebel leader:</b> <a href="https://www.google.com/search?q={leader.column('fullbirthname')}" target="_blank"><u>Click here</u></a></p>
    
      </div>
   {/if}
  </Page>


  <style>
    .search{
      font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
      position: sticky;
      top:15%;
      float: left;
      max-width: 180px;
      margin-left: 20px;
      padding-top: 10px;
      padding-bottom: 20px;
      padding-left: 10px;
      padding-right: 5px;
      background-color: #fff;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      gap: 5px;
    }


    .container {
      max-width: 800px;
      margin: 20px auto;
      padding: 20px;
      background-color: #fff;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      margin-left: 250px
    }
    
  h1 {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    padding-left: 10px;
  }
  
  button:hover {
    background-color: #15b300;
  }
  
    
  a {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    color: #007bff;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  p {
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    margin: 10px 0;
    padding-left: 10px;
  }

  .image-button {
    float: right;
    background-color: #24ba83;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration:none;
    display:inline-block;
    font-size: 14px;
    margin: 4px 20px;
    transition-duration: 0.4s;
    cursor: pointer;
    border-radius: 4px;
    max-width: 40%;
  }

  .image-button:hover {
    text-decoration: none; 
    background-color: #dcf0e9;
    color: rgb(16, 3, 3);
    border: solid 1px;
  }

  .image-button:hover .image-caption {
  color: rgb(16, 3, 3);
  transition-duration: 0.4s;
  }

  .image-caption {
    display: block;
    font-size: 0.7em;
    color: #fff;
    margin-top: 5px;
  }

</style>

