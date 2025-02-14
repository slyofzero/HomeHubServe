<template>
  <ProfessionalsTable :professionals="professionals" />
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";
import { IProfessional, ProfessionalApiRes } from "@/types";
import { useApi } from "@/utils/api";
import ProfessionalsTable from "./ProfessionalsTable.vue";

const professionals = ref<IProfessional[]>([]);
const professoinalsUrl = `${import.meta.env.VITE_API_URL}/admin/professionals`; // prettier-ignore
const { data: professionalsRes, mutate: professionalsMutate } =
  useApi<ProfessionalApiRes>(professoinalsUrl);
watch(professionalsRes, (res) => {
  professionals.value = res.data.data;
});
</script>
