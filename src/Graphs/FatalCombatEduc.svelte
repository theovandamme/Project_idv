<script>
    import { scaleLinear, scaleOrdinal, scaleLog } from 'd3-scale'
    import { Section, RectangleLayer, XAxis, YAxis, YGridLines, XGridLines, DiscreteLegend, Label, Graphic} from '@snlab/florence'
    import DataContainer from '@snlab/florence-datacontainer'
    import { schemeSet3 } from 'd3-scale-chromatic'

    export let DC_raw
    export let width


    
    // export let selectedReligion
    
    let unique_leaders_yap
    let regionColorScale
    let scaleX
    let scaleY
    let padding
    

    
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
            .domain(DC_raw.domain('Region'))
            .range(schemeSet3);


        

        // function handleMouseClick (event) {
        //     console.log(event)
        //     selected_region = event.key
        // }
        // function handleMouseClickElse (event) {
        //     selected_region = ''
        // }
        

padding = { left: 50, bottom: 40, top: 10, right: 10 }
const color = 'rgb(93, 134, 156)'
</script>