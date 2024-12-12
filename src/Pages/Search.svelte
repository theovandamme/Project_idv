<script>
    export let items
    console.log(items)
    import {
      Page,
      Navbar,
      NavbarBackLink,
      Searchbar,
      List,
      ListItem,
    } from 'konsta/svelte';
  
    let searchQuery = '';
    let test = [
      { title: 'FC Ajax' },
      { title: 'FC Arsenal' },
      { title: 'FC Athletic' },
      { title: 'FC Barcelona' },
      { title: 'FC Bayern München' },
      { title: 'FC Bordeaux' },
      { title: 'FC Borussia Dortmund' },
      { title: 'FC Chelsea' },
      { title: 'FC Galatasaray' },
      { title: 'FC Juventus' },
      { title: 'FC Liverpool' },
      { title: 'FC Manchester City' },
      { title: 'FC Manchester United' },
      { title: 'FC Paris Saint-Germain' },
      { title: 'FC Real Madrid' },
      { title: 'FC Tottenham Hotspur' },
      { title: 'FC Valencia' },
      { title: 'FC West Ham United' },
    ];
  
    function handleSearch(e) {
      searchQuery = e.target.value;
    }
  
    function handleClear() {
      searchQuery = '';
    }
  
    function handleDisable() {
      console.log('Disable');
    }
  
    let filteredItems = [];
    /* eslint-disable */
    $: {
      filteredItems = searchQuery
        ? items.filter((item) =>
            item.toLowerCase().includes(searchQuery.toLowerCase())
          )
        : items;
    }
    /* eslint-enable */
  </script>
  
  <Page>
    <Navbar title="Searchbar">    <Searchbar
        slot="subnavbar"
        onInput={handleSearch}
        value={searchQuery}
        onClear={handleClear}
        disableButton
        disableButtonText="Cancel"
        onDisable={handleDisable}
      />
    </Navbar>
    {#if (searchQuery.length >2)}
    <List strong insetMaterial outlineIos>
      {#if filteredItems.length === 0}
        <ListItem title="Nothing found" />
      {/if}
      {#each filteredItems as item (item)}
        <ListItem key={item} title={item} />
      {/each}
    </List>
    {/if}
  </Page>