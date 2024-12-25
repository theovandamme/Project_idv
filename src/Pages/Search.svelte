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
    <Navbar title="Searchbar">    <Searchbar
        slot="subnavbar"
        onInput={handleSearch}
        value={searchQuery}
        onClear={handleClear}
      />
    </Navbar>
    {#if (searchQuery.length >2)}
      {#if possibleItems.length === 0}
        <button>No result found</button>
      {/if}
      {#each possibleItems as item (item)}
        <button on:click={()=>{selectLeader(item), handleClear()}}> {item}</button>

      {/each}
    {/if}

    
    {#if leader}
      <div class = "container"> 

      <h2>{leader.column('fullbirthname')}</h2>
    
      <a class="image-button" href="https://www.google.com/search?q={leader.column('fullbirthname')}+rebel+leader&tbm=isch" target="_blank">View picture of {leader.column('fullbirthname')} </a>
     
      <p>Leader of rebelgroup: {leader.column('groupname')}</p>
      <p>Gender: {leader.column('gender')}</p>
      <p>Born in: {leader.column('yearofbirth')}</p>
      {#if leader.column('yearofdeath') != '' && leader.column('deathcause') != ''}
        <p>Died in: {leader.column('yearofdeath')}</p>
        <p>Deathcause: {leader.column('deathcause')}</p>
      {:else}
        <p>Still alive</p>
      {/if}

      <p>Born in: {leader.column('placeofbirth')}</p>
      <p>Conflict involved: {leader.column('confdesc')}</p>
      <p>Fighting against: {leader.column('stname')}</p>
      <p>Leadership age: {leader.column('leadershipage')}</p>
      <p>Entry method as leader: {leader.column('entrymethod')}</p>
      <p>Level of education achieved: {leader.column('education')}</p>
      <p>Occupation category before rebel leader: {leader.column('occupation')}</p>
      <p>Religion: {leader.column('religion')}</p>

      
      {#if leader.column('married') == 1}
      <p>Married: Yes</p>
      {:else if leader.column('married') == 0}
      <p>Married: No</p>
      {:else}
       <p>Married: No data available</p>
      {/if}

      {#if leader.column('children') == 1}
      <p>Any children: Yes</p>
      {:else if leader.column('married') == 0}
      <p>Any children: No</p>
      {:else}
       <p>Any children: No data available</p>
      {/if}
      
      {#if leader.column('military') == 1}
      <p>Military experience before rebel leader: Yes</p>
      {:else if leader.column('military') == 0}
      <p>Military experience before rebel leader: No</p>
      {:else}
       <p>Military experience before rebel leader: No data available</p>
      {/if}

      {#if leader.column('combat') == 1}
      <p>Previous combat experience before becoming rebel leader: Yes</p>
      {:else if leader.column('combat') == 0}
      <p>Previous combat experience before becoming rebel leader: No</p>
      {:else}
       <p>Previous combat experience before becoming rebel leader: No data available</p>
      {/if}

      {#if leader.column('govpost') == 1}
      <p>Government post before becoming rebel leader: Yes</p>
      {:else if leader.column('govpost') == 0}
      <p>Government post before becoming rebel leader: No</p>
      {:else}
       <p>Government post before becoming rebel leader: No data available</p>
      {/if}

      {#if leader.column('exile') == 1}
      <p>Been in exile before becoming rebel leader: Yes</p>
      {:else if leader.column('exile') == 0}
      <p>Been in exile before becoming rebel leader: No</p>
      {:else}
       <p>Been in exile before becoming rebel leader: No data available</p>
      {/if}

      {#if leader.column('studyab') == 1}
      <p>Studied abroad before becoming rebel leader: Yes</p>
      {:else if leader.column('studyab') == 0}
      <p>Studied abroad before becoming rebel leader: No</p>
      {:else}
       <p>Studied abroad before becoming rebel leader: No data available</p>
      {/if}

      {#if leader.column('workab') == 1}
      <p>Worked abroad before becoming rebel leader: Yes</p>
      {:else if leader.column('workab') == 0}
      <p>Worked abroad before becoming rebel leader: No</p>
      {:else}
       <p>Worked abroad before becoming rebel leader: No data available</p>
      {/if}

      {#if leader.column('prison') == 1}
      <p> Imprisoned before becoming rebel leader: Yes</p>
      {:else if leader.column('prison') == 0}
      <p>Imprisoned before becoming rebel leader: No</p>
      {:else}
       <p>Imprisoned before becoming rebel leader: No data available</p>
      {/if}

      <p> Do you want more info about the rebel leader? <a href="https://www.google.com/search?q={leader.column('fullbirthname')}" target="_blank">Click here</a></p>
    
      </div>
   {/if}
  </Page>


  <style>
    .container {
      max-width: 800px;
      margin: 20px auto;
      padding: 20px;
      background-color: #fff;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }
    
  h2 {
    padding-left: 10px;
  }
  
  button:hover {
    background-color: #15b300;
  }
  
    
  a {
    color: #007bff;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  p {
    margin: 10px 0;
    padding-left: 10px;
  }

  .image-button {
    float: right;
    margin-left: 10px;
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border-radius: 4px;
    display: inline-block;
  }

  .image-button:hover {
    background-color: #0056b3;
    text-decoration: none;
  }

</style>

