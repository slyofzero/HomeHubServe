<template>
  <ProfessionalsTable
    :professionals="professionals"
    :show-view-all="false"
    @refreshProfessionals="mutateProfessionals"
  />
  <Pagination :url="professionalsUrl" :limit="10" v-model="professionals" />
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";
import { IProfessional, ProfessionalApiRes } from "@/types";
import { clientFetcher, useApi } from "@/utils/api";
import { ProfessionalsTable } from "@/components/professionals";
import Pagination from "../Pagination.vue";

const page = ref<number>(1);
const totalPages = ref<number>(1);

const professionals = ref<IProfessional[]>([]);
const professionalsUrl = `${import.meta.env.VITE_API_URL}/admin/professionals`;
const { data: professionalsRes, mutate: mutateProfessionals } =
  useApi<ProfessionalApiRes>(professionalsUrl);

watch(page, async () => {
  const res = await clientFetcher<ProfessionalApiRes>(professionalsUrl);
  if (res.data.data) {
    professionals.value = res.data.data;
    totalPages.value = res.data.totalPages;
  }
});

watch(professionalsRes, (res) => {
  if (res.data.data) {
    professionals.value = res.data.data;
    totalPages.value = res.data.totalPages;
  }
});
</script>
