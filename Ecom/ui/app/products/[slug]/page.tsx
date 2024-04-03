import Image from 'next/image'
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
  } from "@/components/ui/accordion"  
import {
  ToggleGroup,
  ToggleGroupItem,
} from "@/components/ui/toggle-group"
import { getProducts } from '@/actions/getProduct'
import { IProducts } from '@/components/Products'

interface IPage{
    params : {
        slug: string
    }
}

const page = async ({params}: IPage) => {
    const product: IProducts = await getProducts(params.slug)
    const images = [product.image1, product.image2]
  return (
    <div className='mt-14 mb-10'>
        <div className='grid lg:grid-cols-2 gap-8 mx-10 shadow-lg rounded-lg'>
            <div className='flex justify-center space-x-1 lg:col-span-1'>
                {images.map((img, index) => {
                    return(
                        <div key={index} className='flex space-x-4'>
                        <Image src={img} alt={product.name} key={index} className='rounded-t-lg object-cover' width={850} height={1150} />
                        </div>
                    )
                }
        )}
            </div>
            <div className='lg:col-span-1'>
            <div className='w-full h-min border basis-60 border-zinc-800 rounded bg-zinc-900'>
                <div className='flex flex-col justify-between gap-3 p-5 border-b border-zinc-800'>
                    <h2 className='text-xl font-semibold'>{product.name}</h2>
                    <span className='text-xl font-semibold'>${product.price}</span>
                    <p className='mt-2 text-sm '>{product.description}</p>
                </div>
                <div className='py-5'>
                    <ToggleGroup type='single' className='grid grid-cols-4 border-zinc-800 px-5 space-x-2.5 justify-center'>
                        <ToggleGroupItem value='S' className='flex items-center hover:border-zinc-400 border-zinc-800 justify-center border px-1 py-1.5 bg-black rounded 
                            transition duration-150 ease text-13'>
                                <span>S</span>
                        </ToggleGroupItem>
                        <ToggleGroupItem value='M' className='flex items-center hover:border-zinc-400 border-zinc-800 justify-center border px-1 py-1.5 bg-black rounded 
                            transition duration-150 ease text-13'>
                                <span>M</span>
                        </ToggleGroupItem>
                        <ToggleGroupItem value='L' className='flex items-center hover:border-zinc-400 border-zinc-800 justify-center border px-1 py-1.5 bg-black rounded 
                            transition duration-150 ease text-13 '>
                                <span>L</span>
                        </ToggleGroupItem>
                        <ToggleGroupItem value='XL' className='flex items-center justify-center border hover:border-zinc-400 border-zinc-800 px-1 py-1.5 bg-black rounded 
                            transition duration-150 ease text-13 '>
                                <span>XL</span>
                        </ToggleGroupItem>
                    </ToggleGroup>
                </div>
                <div className='border-t border-zinc-800 '>
                    <button className='w-full hover:bg-[#1F1F1F] border-zinc-800 p-2 transition duration-150 text-13 ease border'>Add to Cart</button>
                </div>
            </div>
            <Accordion type="single" className='py-5' collapsible>
                <AccordionItem value="item-1" className='border-zinc-800'>
                    <AccordionTrigger className='hover:no-underline'>Composition</AccordionTrigger>
                    <AccordionContent>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-2" className='border-zinc-800'>
                    <AccordionTrigger className='hover:no-underline'>Care</AccordionTrigger>
                    <AccordionContent>
                    Ratione nobis, voluptatum quia quis magnam repellat quibusdam qui! Rem quidem accusantium modi
                    </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-3" className='border-zinc-800'>
                    <AccordionTrigger className='hover:no-underline'>Origin</AccordionTrigger>
                    <AccordionContent>
                    rerum ipsa voluptatem dolorum. Esse numquam debitis officiis ipsam.
                    </AccordionContent>
                </AccordionItem>
            </Accordion>
            </div>
        </div>
    </div>
  )
}

export default page