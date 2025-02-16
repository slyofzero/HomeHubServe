<template>
  <div class="mb-4">
    <div class="d-flex flex-column gap-4 p-4">
      <h4>All Services</h4>
    </div>

    <div class="d-flex flex-column justify-content-center gap-4 container">
      <div
        class="row"
        v-for="(row, rowIndex) in servicesToDisplay"
        :key="rowIndex"
      >
        <div class="col-md-3 mb-3" v-for="(service, index) in row" :key="index">
          <ServiceCard :service="service" />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { IService, ServiceApiRes } from "@/types";
import { useApi } from "@/utils/api";
import { computed, ref, watch } from "vue";
import { chunkArray } from "@/utils/general";
import { ServiceCard } from ".";

const services = ref<IService[]>([]);
const servicesUrl = `${import.meta.env.VITE_API_URL}/service`;
const { data: serviceRes } = useApi<ServiceApiRes>(servicesUrl);

watch(serviceRes, () => {
  const new_services = serviceRes.value?.data.data;
  services.value = new_services ? new_services : [];
});

const servicesToDisplay = computed(() => chunkArray(services.value, 4));
</script>
