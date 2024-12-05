<script>
    import { Graphic, Section, RectangleLayer, PointLayer, Line, XAxis, YAxis } from '@snlab/florence'
    import { regressionLinear } from 'd3-regression'
    import { scaleLinear, scaleBand, scaleTime } from 'd3-scale'
    import DataContainer from '@snlab/florence-datacontainer'
    export let DC_raw
    export let selected_region


    let DC
    $: DC = DC_raw

    $: columnNames = DC.columnNames()

    function makeArrayfromRow(Row){
        let NewArray = []
        for (let item of columnNames){
            let element = Row[item] 
            if (typeof element == 'string' && element.includes(';')){ 
                let new_elemenent = element.replaceAll(';', '/')
                NewArray.push(new_elemenent)
            } else {
                NewArray.push(element)
            }
        }
        return NewArray
    }
    function makeArrayFromWholeDC(DC){
        let NewArray = [columnNames]
        for (let i=0; i< DC.nrow(); i++) {
            NewArray.push(makeArrayfromRow(DC.row({index:i})))
        }
        return NewArray
    }
    function makeCSV(DC) {
        let csvContent = ''
        let refined_DC = makeArrayFromWholeDC(DC)
        refined_DC.forEach(row => {
        csvContent += row.join(';') + '\n'
        })
        let blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8,' })
        let objUrl = URL.createObjectURL(blob)
        return objUrl
    }

</script>
    
      <button class='selector'>
        <a href={makeCSV(DC)} download= {'ROLE_'.concat(selected_region).concat(".csv")} id="link">Download {selected_region} data as CSV</a>
      </button>

<style>
.selector{width: 42.5%;
        margin-left:5%}
</style>