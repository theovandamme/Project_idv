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

    //{leader.column(‘fullbirthname’)}


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
        <button  on:click={()=>{selectLeader(item), handleClear()}}> {item}</button>

      {/each}
    {/if}
    <div> 
      {#if leader}
      {leader.column('fullbirthname')}
      {/if}
      
    
    
    
      </div>
  </Page>
  

