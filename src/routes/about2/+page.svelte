<script>
    import PageLayout from "$lib/layout/PageLayout.svelte"
    import TemperatureConverter from "$lib/components/TemperatureConverter.svelte"
</script>


<PageLayout>
    <div slot="main-block-content">
        <p style="text-align: center;">About Center</p>
        <TemperatureConverter/>
    </div>
    <div slot="left-menu-content">
        <p style="text-align: center;">About Left</p>
    </div>
    <div slot="right-menu-content">
        <p style="text-align: center;">About Right</p>
    </div>
</PageLayout>