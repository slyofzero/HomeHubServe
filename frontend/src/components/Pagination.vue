<template>
  <div class="d-flex flex-column gap-2">
    <div class="text-center">
      <span class="d-inline-block"> Page {{ page }} of {{ totalPages }} </span>
    </div>

    <nav>
      <ul class="d-flex justify-content-center pagination">
        <li class="page-item">
          <button
            @click="startPage"
            class="page-link btn"
            :disabled="page == 1"
          >
            Start
          </button>
        </li>
        <li class="page-item">
          <button
            @click="previousPage"
            class="page-link btn"
            :disabled="page == 1"
          >
            Previous
          </button>
        </li>
        <li class="page-item" v-for="page in availablePages">
          <button class="page-link btn">{{ page }}</button>
        </li>
        <li class="page-item">
          <button
            @click="nextPage"
            class="page-link btn"
            :disabled="page == totalPages"
          >
            Next
          </button>
        </li>
        <li class="page-item">
          <button
            @click="endPage"
            class="page-link btn"
            :disabled="page == totalPages"
          >
            End
          </button>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script lang="ts" setup>
import { computed, onMounted, ref, watch } from "vue";
import { clientFetcher, useApi } from "@/utils/api";
import { ApiRes } from "@/types";

interface Props {
  url: string;
  limit: number;
  modelValue: any[];
}
const props = defineProps<Props>();
const emit = defineEmits(["update:modelValue"]);

const page = ref<number>(1);
const totalPages = ref<number>(1);
const availablePages = computed(() => {
  const maxPagesToShow = 3;
  const pages: number[] = [];

  let startPage = Math.max(1, page.value - Math.floor(maxPagesToShow / 2));
  let endPage = startPage + maxPagesToShow - 1;

  if (endPage > totalPages.value) {
    endPage = totalPages.value;
    startPage = Math.max(1, endPage - maxPagesToShow + 1);
  }

  for (let i = startPage; i <= endPage; i++) {
    pages.push(i);
  }

  return pages;
});

const url = computed(() => `${props.url}?page=${page.value}&limit=${props.limit}`); // prettier-ignore

const fetchData = async () => {
  try {
    const res = await clientFetcher<ApiRes>(url.value);
    if (res.data.data) {
      emit("update:modelValue", res.data.data);
      totalPages.value = res.data.totalPages;
    }
  } catch (error) {
    console.error("API Error:", error);
  }
};

watch(page, fetchData, { immediate: true });

const startPage = () => {
  page.value = 1;
};

const endPage = () => {
  page.value = totalPages.value;
};

const previousPage = () => {
  if (page.value > 1) {
    page.value -= 1;
  }
};

const nextPage = () => {
  if (page.value < totalPages.value) {
    page.value += 1;
  }
};
</script>
