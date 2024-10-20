import{a as n}from"./CCb-kr4I.js";import{_ as d,c as b,a as o,n as u,p as i,v as a,o as m}from"./BSKXyNXC.js";var p={};const g={data(){return{email:"",password:""}},methods:{async submit(){try{const t=p.API_BASE_URL||"http://localhost:3000";await n.post(`${t}/api/auth/login`,{email:this.email,password:this.password})}catch(t){console.error("Error logging in:",t)}},loginWithGoogle(){},loginWithFacebook(){}}},c={class:"min-h-screen flex flex-col justify-center items-center bg-cover"},f={class:"bg-white p-8 rounded-lg shadow-lg w-full max-w-md"},w={class:"mb-4"},x={class:"mb-4"},h={class:"flex flex-col space-y-4"};function y(t,e,v,k,r,l){return m(),b("div",c,[o("div",f,[e[8]||(e[8]=o("h1",{class:"text-3xl font-bold mb-8 text-center"}," Iniciar Sessió ",-1)),o("form",{onSubmit:e[2]||(e[2]=u((...s)=>l.submit&&l.submit(...s),["prevent"]))},[o("div",w,[e[5]||(e[5]=o("label",{class:"block text-gray-700",for:"email"},"Email",-1)),i(o("input",{id:"email","onUpdate:modelValue":e[0]||(e[0]=s=>r.email=s),class:"form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300",type:"email",required:"",placeholder:"Email"},null,512),[[a,r.email]])]),o("div",x,[e[6]||(e[6]=o("label",{class:"block text-gray-700",for:"password"},"Contrasenya",-1)),i(o("input",{id:"password","onUpdate:modelValue":e[1]||(e[1]=s=>r.password=s),class:"form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300",type:"password",required:"",placeholder:"Contrasenya"},null,512),[[a,r.password]])]),e[7]||(e[7]=o("button",{class:"bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700 w-full mb-4",type:"submit"}," Iniciar Sessió ",-1))],32),o("div",h,[o("button",{class:"bg-red-500 text-white py-2 px-4 rounded hover:bg-red-700 w-full",onClick:e[3]||(e[3]=(...s)=>l.loginWithGoogle&&l.loginWithGoogle(...s))}," Iniciar Sessió amb Google "),o("button",{class:"bg-blue-800 text-white py-2 px-4 rounded hover:bg-blue-900 w-full",onClick:e[4]||(e[4]=(...s)=>l.loginWithFacebook&&l.loginWithFacebook(...s))}," Iniciar Sessió amb Facebook ")])])])}const _=d(g,[["render",y]]);export{_ as default};
